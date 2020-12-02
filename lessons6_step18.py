from selenium import webdriver
import time
import math


def calc(x):
  return str(math.log(abs(12*math.sin(int(x))))) 


link='http://suninjuly.github.io/alert_accept.html'
browser = webdriver.Chrome()
browser.get(link)
submit_btn = browser.find_element_by_css_selector('[type="submit"]').click()
confirm = browser.switch_to.alert
confirm.accept() 
try:
    x_element = browser.find_element_by_id("input_value") 
    x = x_element.text
    y = calc(x)

    answer = browser.find_element_by_id("answer")
    answer.send_keys(y)
    
    submit_btn = browser.find_element_by_css_selector('[type="submit"]').click()
    

finally:
    # 
    time.sleep(30)
    # 
    browser.quit()

# 