import re
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options


def func(name):
    result = []
    chrome_options = Options()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--disable-gpu')
    chrome_options.add_argument('window-size=1200x600')
    browser = webdriver.Chrome(chrome_options=chrome_options)
    while 1:
        browser.get('https://image.baidu.com')
        time.sleep(1)
        input = browser.find_element_by_id('kw')
        break
    input.send_keys(name)
    input.send_keys(Keys.ENTER)
    js = "window.scrollTo(0,1000);"
    browser.execute_script(js)
    time.sleep(2)
    urls = browser.find_elements_by_xpath("//div[@class='imgbox']//a")
    for url in urls[0:5]:
        n_url = url.get_attribute("href")
        driver = webdriver.Chrome(chrome_options=chrome_options)
        # driver = webdriver.Chrome()
        time.sleep(1)
        while 1:
            try:
                driver.get(n_url)
                break
            except:
                pass
        try:
            image_url = driver.find_element_by_xpath('//*[@id="currentImg"]').get_attribute("src")
        except:
            continue
        print(image_url)
        time.sleep(2)
        try:
            driver.find_element_by_xpath("//div[@class='pic-title']//a").click()
        except:
            continue
        time.sleep(1)
        windows = driver.window_handles
        driver.switch_to.window(windows[-1])
        try:
            html = driver.page_source
        except:
            driver.close()
            driver.quit()
            continue
        text = ''
        for n in re.findall(r'[\u4e00-\u9fff]+', html):
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
