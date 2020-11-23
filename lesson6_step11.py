from selenium import webdriver
import time
import math


link = "http://suninjuly.github.io/math.html"

def calc(x):
  return str(math.log(abs(12*math.sin(int(x))))) 


try:
    browser = webdriver.Chrome()
    browser.get(link)

    x_element = browser.find_element_by_id("input_value")
    x = x_element.text
    y = calc(x)

    answer = browser.find_element_by_id("answer")
    answer.send_keys(y)
    
    checkbox = browser.find_element_by_css_selector("#robotCheckbox").click()
    radio_btn = browser.find_element_by_css_selector("#robotsRule").click()
    submit_btn = browser.find_element_by_css_selector('[type="submit"]').click()
    

finally:
    # 
    time.sleep(30)
    # 
    browser.quit()

# 