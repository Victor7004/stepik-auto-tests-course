from selenium import webdriver
import time
import math


def calc(x):
  return str(math.log(abs(12*math.sin(int(x))))) 


link='http://suninjuly.github.io/redirect_accept.html'
browser = webdriver.Chrome()
browser.get(link)
submit_btn = browser.find_element_by_css_selector('[type="submit"]').click()
time.sleep(2)
new_window = browser.window_handles[1]
browser.switch_to.window(new_window) 
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