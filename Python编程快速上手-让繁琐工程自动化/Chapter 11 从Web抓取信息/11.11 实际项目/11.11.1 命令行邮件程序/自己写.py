from selenium import webdriver
browser = webdriver.Chrome()
url = 'https://mail.qq.com/cgi-bin/loginpage'
browser.get(url)
usernameInput = browser.find_element_by_id('u')
usernameInput.send_keys('yirufeng@foxmail.com')
passwordInput = browser.find_element_by_id('p')
passwordInput.send_keys('1018222WXW')
submitButton = browser.find_element_by_id('login_button')
submitButton.click()



