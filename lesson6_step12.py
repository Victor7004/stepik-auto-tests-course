from selenium import webdriver
import time
import math


link = "http://suninjuly.github.io/get_attribute.html"

def calc(x):
  return str(math.log(abs(12*math.sin(int(x))))) 


try:
    browser = webdriver.Chrome()
    browser.get(link)


    img_treasure = browser.find_element_by_id("treasure")
    x_element = img_treasure.get_attribute("valuex")
    x = x_element
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