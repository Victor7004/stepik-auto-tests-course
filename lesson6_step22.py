from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x))))) 

browser = webdriver.Chrome()
browser.get("http://suninjuly.github.io/explicit_wait2.html")

try:
    element1 = WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "$100")
    )
    button = WebDriverWait(browser, 15).until(
        EC.element_to_be_clickable((By.ID, "book"))
    )

    button.click()

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