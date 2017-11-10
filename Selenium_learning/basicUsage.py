# -*- coding: utf-8 -*-

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# browser = webdriver.Chrome('/Users/xiongyi/Downloads/chromedriver')
# browser.get('http://www.baidu.com/')  # 用google浏览器打开www.baidu.com

driver = webdriver.Chrome('/Users/xiongyi/Downloads/chromedriver')
driver.get("http://www.python.org")
assert "Python" in driver.title
elem = driver.find_element_by_name("q")
elem.send_keys("pycon")
elem.send_keys(Keys.RETURN) # 使用Keys类来模拟键盘输入
print driver.page_source # 获取网页渲染后的源代码
