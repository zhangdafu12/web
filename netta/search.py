# coding:utf-8
# _author_:Junjie
# date:2018/12/13

import logging
import re
import datetime
from selenium.webdriver.chrome.options import Options

logname = "baidu.log"
filehandler = logging.FileHandler(filename=logname, encoding="utf-8")
fmter = logging.Formatter(fmt="%(asctime)s %(message)s", datefmt="%Y-%m-%d %H:%M:%S")
filehandler.setFormatter(fmter)
loger = logging.getLogger(__name__)
loger.addHandler(filehandler)
loger.setLevel(logging.FATAL)
loger.fatal("second log")


def getFirsttimeasFormated(test_str):
    pattern = re.compile(
        r'((?P<year>\d{2,4})(-|/|年|\s)(?P<mouth>\d{1,2})(-|/|月|\s)(?P<day>\d{1,2})(\s|-|日|)*)((?P<hour>\d{1,2})(:|-|\s)(?P<min>\d{1,2})((:|-|\s)(?P<sec>\d{1,2}))*)*')
    mat = pattern.search(test_str)
    year = mat.groupdict().get('year')
    mouth = mat.groupdict().get('mouth')
    day = mat.groupdict().get('day')
    hour = mat.groupdict().get('hour')
    min = mat.groupdict().get('min')
    sec = mat.groupdict().get('sec')
    if year == None:
        return None
    if len(year) == 4:
        tempyear = '%Y'
    if len(year) == 2:
        tempyear = '%y'
    if hour == None:
        result = datetime.datetime.strptime(year + '-' + mouth + '-' + day, tempyear + '-%m-%d')
    elif sec == None:
        result = datetime.datetime.strptime(year + '-' + mouth + '-' + day + '-' + hour + '-' + min,
                                            tempyear + '-%m-%d-%H-%M')
    else:
        result = datetime.datetime.strptime(year + '-' + mouth + '-' + day + '-' + hour + '-' + min + '-' + sec,
                                            tempyear + '-%m-%d-%H-%M-%S')
    return result


def datetime_toString(dt):
    return dt.strftime("%Y-%m-%d %H:%M:%S")


def getPureTitlefrom_webTitle(redunTitle):
    import re
    splitArray = re.split('_|-', redunTitle)
    if len(splitArray) > 2:  # 此时无法区分出真正的题目
        return redunTitle
    title = (re.split('_|-', redunTitle))[0].strip(' ')  # 不同家的新闻会使用各自不同的符号，后跟自己的网站名称
    return title


def getMiddlePart(bodyWeb):
    # print('t')
    end_list = [r'阅读全文: http://', '版权声明：本文为博主原创文章，未经博主允许不得转载', '想对作者说点什么？', '如你有好的文章想和大家分享欢迎投稿', '文章标签：', '个人分类：',
                '未经作者许可，不得转载', '文章仅代表作者个人观点，不代表百度立场']

    text = bodyWeb[0]
    title = bodyWeb[1]
    title = getPureTitlefrom_webTitle(title)  # 不同家的新闻会使用各自不同的符号，后跟自己的网站名称


def baidu_search_service(url):
    result_list = []
    from selenium import webdriver
    chrome_options = Options()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--disable-gpu')
    chrome_options.add_argument('window-size=1200x600')
    browser = webdriver.Chrome(chrome_options=chrome_options)
    browser.maximize_window()
    browser.get(url)
    # browser.set_page_load_timeout(40)
    # browser.set_script_timeout(40)
    realUrl = browser.current_url  # 此处的realUrl为真实的url
    print(realUrl)
    realtitle = browser.title
    page_text = browser.find_element_by_css_selector("body").text
    try:
        web_time = getFirsttimeasFormated(page_text)
    except Exception as ex1:
        web_time = ''
        print(ex1)
    if not type(web_time) == str:
        web_time = web_time.strftime("%Y%m%d%H%M%S")
    result_list.append((realUrl, realtitle, web_time, page_text, realtitle, ''))

    print(result_list)
    return result_list


if __name__ == '__main__':
    baidu_search_service('http://liaoyang.nen.com.cn/76850369518370816/20091021/2192708.shtml')
