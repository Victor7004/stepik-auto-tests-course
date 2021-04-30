from selenium import webdriver
from selenium.common.exceptions import NoAlertPresentException
#from selenium.webdriver.common.by import By(импорт не нужен и закоментирован)
import time
import math


link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcodershandbook_209/?promo=newYear"

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

#def solve_quiz_and_get_code(self):
    #alert = self.browser.switch_to.alert
    #x = alert.text.split(" ")[2]
    #answer = str(math.log(abs((12 * math.sin(float(x))))))
    #alert.send_keys(answer)
    #alert.accept()
    #try:
        #alert = self.browser.switch_to.alert
        #alert_text = alert.text
        #print(f"Your code: {alert_text}")
        #alert.accept()
    #except NoAlertPresentException:
        #print("No second alert presented") 
browser = webdriver.Chrome()
browser.get(link) 
button = browser.find_element_by_css_selector("button.btn-add-to-basket") 
button.click() 
    #solve_quiz_and_get_code(self)
time.sleep(2)
new_window = browser.window_handles[0]
browser.switch_to.window(new_window)
try:
    x_element = browser.find_element_by_id("input_value")
    x = x_element.text
    y = calc(x)

    answer = browser.find_element_by_id("answer")
    answer.send_keys(y)

    submit = browser.find_element_by_css_selector('[type="submit"]').click() 
 

    #x_element = browser.find_element_by_id("input_value")
    #x = x_element.text
    #y = calc(x)

    #answer = browser.find_element_by_id("answer")
    #answer.send_keys(y)

finally:
    #
    time.sleep(30)
    #
    browser.quit()

    #
