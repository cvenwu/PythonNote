from selenium import webdriver
browser = webdriver.Chrome()
browser.get('http://www.baidu.com')
search_content = browser.find_element_by_id('kw')
search_content.send_keys('百度')
search_content.submit()
