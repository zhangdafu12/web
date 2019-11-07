import re
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

def func(name):
    result = []
    browser = webdriver.Chrome()

    browser.get('https://image.baidu.com')
    time.sleep(1)
    input = browser.find_element_by_id('kw')
    input.send_keys(name)
    input.send_keys(Keys.ENTER)
    js = "window.scrollTo(0,1000);"
    browser.execute_script(js)
    time.sleep(2)
    urls = browser.find_elements_by_xpath("//div[@class='imgbox']//a")
    # imgs = browser.find_elements_by_xpath("//div[@class='imgbox']//a//img")

    # for img in imgs[0:5]:
    #     data_imgurl = img.get_attribute("data-imgurl")
    #     print(data_imgurl)

    for url in urls[0:5]:
        n_url = url.get_attribute("href")
        driver = webdriver.Chrome()
        time.sleep(1)
        driver.get(n_url)
        try:
            image_url = driver.find_element_by_xpath('//*[@id="currentImg"]').get_attribute("src")
        except:
            continue
        print(image_url)
        time.sleep(2)
        driver.find_element_by_xpath("//div[@class='pic-title']//a").click()
        time.sleep(1)
        windows = driver.window_handles
        driver.switch_to.window(windows[-1])
        # now_url = driver.current_url
        html = driver.page_source
        text = ''
        for n in re.findall(r'[\u4e00-\u9fff]+', html):
            # print(n)
            text += n
        result.append((image_url,text))
        driver.close()
        driver.quit()
    browser.quit()
    print(result)
    return result


if __name__ == '__main__':
    name = input('请输入:')
    func(name=name)
