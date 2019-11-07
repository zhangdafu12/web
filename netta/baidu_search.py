# coding:utf-8
# _author_:Junjie
# date:2019/7/14
import re
import datetime
from selenium.webdriver.chrome.options import Options


def getFirsttimeasFormated(test_str):
    pattern = re.compile(r'((?P<year>\d{2,4})(-|/|年|\s)(?P<mouth>\d{1,2})(-|/|月|\s)(?P<day>\d{1,2})(\s|-|日|)*)((?P<hour>\d{1,2})(:|-|\s)(?P<min>\d{1,2})((:|-|\s)(?P<sec>\d{1,2}))*)*')
    mat = pattern.search(test_str)
    year = mat.groupdict().get('year')
    mouth = mat.groupdict().get('mouth')
    day = mat.groupdict().get('day')
    hour = mat.groupdict().get('hour')
    min = mat.groupdict().get('min')
    sec = mat.groupdict().get('sec')
    if year==None:
        return None
    if len(year)==4:
        tempyear = '%Y'
    if len(year)==2:
        tempyear = '%y'
    if hour==None :
        result = datetime.datetime.strptime(year+'-'+mouth+'-'+day,tempyear+'-%m-%d')
    elif sec == None:
        result = datetime.datetime.strptime(year+'-'+mouth+'-'+day+'-'+hour+'-'+min,tempyear+'-%m-%d-%H-%M')
    else:
        result = datetime.datetime.strptime(year+'-'+mouth+'-'+day+'-'+hour+'-'+min+'-'+sec,tempyear+'-%m-%d-%H-%M-%S')
    return result


def datetime_toString(dt):
    return  dt.strftime("%Y-%m-%d %H:%M:%S")


def getPureTitlefrom_webTitle(redunTitle):
    import re
    splitArray = re.split('_|-', redunTitle)
    if len(splitArray) > 2:  # 此时无法区分出真正的题目
        return redunTitle
    title = (re.split('_|-', redunTitle))[0].strip(' ')  # 不同家的新闻会使用各自不同的符号，后跟自己的网站名称
    return title


def baidu_search_service2(search_key, result_num):
    result_list = []
    from selenium import webdriver
    import time

    # from JiebaAnalys.anylysis import branchCommonInfo
    search_key = str(search_key)
    print('baidu-Search' + str(time.time()))
    personName = search_key.split(' ')[0]

    num = result_num + 1  # num 作为搜索结果总数，恒定不变，用于控制产生的结果页面文件名的序号值，

    chrome_options = Options()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--disable-gpu')
    chrome_options.add_argument('window-size=1200x600')
    browser = webdriver.Chrome(chrome_options=chrome_options)
    browser.maximize_window()
    browser.get("https://www.baidu.com/")
    browser.implicitly_wait(3)
    browser.find_element_by_id("kw").send_keys( search_key.replace('_', ' '))
    browser.find_element_by_id("su").click()
    browser.set_page_load_timeout(40)
    browser.set_script_timeout(40)
    # print('line49')
    url_txt_tuple_set = []
    time.sleep(5)
    for i in range(0, result_num // 10):
        results = browser.find_elements_by_css_selector("#content_left > .c-container")
        # print('line53')
        if len(results) == 0:
            # print("没有找到与“" + search_key + "”相关的网页。 ")
            break
        for j in range(0, len(results)):
            pageOrder = num - result_num
            # print(pageOrder)
            # print(j)
            try:
                # result = browser.find_element_by_id(str(j+1))
                # print("exception 64")
                result = browser.find_element_by_id(str(pageOrder))
                title = result.find_element_by_css_selector('h3 > a').text
                print(title)
                description = result.find_element_by_css_selector('div.c-abstract').text
                print(description)
                # print("exception 66")
                try:
                    # print("exception 68")
                    web_time = result.find_element_by_class_name('newTimeFactor_before_abs').text
                    # print(web_time)
                except Exception as e:
                    web_time = ""
                    # print("webtime exception 68")
                    print(e)
            except Exception as e:
                print(e)
                # print(" exception 71")
                # print("该关键字只存在 " + str(pageOrder) + "条记录！" + str(e) + ' at line 130')
                result_num -=1
                # i = -1
                continue
            try:
                _ins_fakedurl = result.find_element_by_css_selector("h3 > a").get_attribute("href")

            except Exception as es:
                print(es)
                # print('82')
                break


            while True:
                try:
                    js = "window.open('" + _ins_fakedurl + "');"
                    browser.execute_script(js)
                    handles = browser.window_handles
                    browser.switch_to_window(handles[1])
                    realUrl = browser.current_url  # 此处的realUrl为真实的url
                    print(realUrl)
                    realtitle = browser.title
                    # print('at line 94')
                    # print(realUrl)

                    if realUrl.find('image.baidu.com') > -1:
                        # print('at line 103')
                        # browser.close()
                        # browser.switch_to_window(handles[0])
                        # print('at line 106')
                        # print(realUrl + '   is passed for image_baidu!!!!!!')
                        break
                    try:
                        # source_code = browser.page_source
                        page_text = browser.find_element_by_css_selector("body").text
                        if web_time == '':
                            try:
                                web_time = getFirsttimeasFormated(page_text)# 将网页body里，标题下面的时间格式化
                            except Exception as ex1:

                                print(ex1)

                        try:
                            if web_time == '':
                                # print('at line 116')
                                web_time = getFirsttimeasFormated(browser.page_source)
                        except Exception as ex1:
                            # print('line 114 of web_time')
                            print(ex1)
                        if type(web_time) == datetime.datetime:
                            web_time = datetime_toString(web_time)
                        # browser.close()
                        # browser.switch_to_window(handles[0])
                        try:


                            # page_text2 = getMiddlePart((page_text,realtitle))
                            # # print('at line 129')
                            # if page_text2:
                            #     page_text = page_text2
                            result_list.append((realUrl, realtitle, web_time, page_text,title,description))
                            # print(realUrl)
                            # print('at line 126')

                        except Exception as es:
                            print(es)
                            print('getMiddlePart in baidu -search error')
                            # loger.error(realtitle + '  from the url of  ' + realUrl)
                            # loger.error(' generating error  in  founding   ' + search_key + '  at  '+  time.ctime())
                            # browser.close()
                            # browser.switch_to_window(handles[0])
                            break
                    except Exception as e:
                        print(e)
                        print('at line 130')
                        # loger.error(e)
                        # browser.close()
                        # browser.switch_to_window(handles[0])
                        # print("第" + str(pageOrder) + "条数据出现异常！" + str(e) + ' at line 156')
                        # 将访问出错的网页，非timeout错误，放入指定url记录队列
                        # branchCommonInfo.notElefound_in_Web_exceptionUrl_queue.add(realUrl)
                        break
                    if page_text.find(personName) > -1:
                        # idendtify_Url_scanned(search_key, realUrl)
                        url_txt_tuple_set.append((realUrl, page_text))

                        # branchCommonInfo.add_New_Url(realUrl)
                        # branchCommonInfo.web_scanned_count += 1
                    break
                except Exception as e:
                    # print('at line 159')
                    print(e)
                    # print('  at line 146')
                    # loger.error(e)
                    # print("time out error " + str(e) + ' at line 199')
                    # browser.close()
                    # browser.switch_to_window(handles[0])
                    # continue
                    break
            try:
                browser.close()
            except:
                pass
            browser.switch_to_window(handles[0])
            result_num -= 1
        if i != -1:
            # 点击下一页
            try:
                pages = browser.find_elements_by_css_selector("#page > a")
            except Exception as e:
                print(e)
                # print( 'at 160')
                break
            for page in pages:
                browser.execute_script("arguments[0].scrollIntoView();", page)
                if page.text == '下一页>':
                    page.click()
                    break
        else:
            break
        time.sleep(5)
    browser.close()
    # result_list = pickle.dumps(result_list)
    print('search finished in baidu search.py')
    return result_list

if __name__ == '__main__':
    result = baidu_search_service2('王思聪',10)
    print(result)