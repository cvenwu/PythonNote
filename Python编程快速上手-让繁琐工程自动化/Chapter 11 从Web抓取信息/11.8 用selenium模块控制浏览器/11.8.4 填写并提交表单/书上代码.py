from selenium import webdriver
browser = webdriver.Chrome()
browser.get('http://gmail.com')
emailElem = browser.find_element_by_id('Email')
emailElem.send_keys('not_my_real_email@gmail.com')
passwordElem = browser.find_element_by_id('Passwd')
passwordElem.send_keys('12345')
passwordElem.submit()