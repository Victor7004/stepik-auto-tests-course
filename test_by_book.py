import pytest
from selenium import webdriver
from selenium.common.exceptions import NoAlertPresentException
import math
import time


def test_guest_should_see_login_link(browser):
    link = f"http://selenium1py.pythonanywhere.com/catalogue/the-shellcodershandbook_209/?promo=newYear" 
    browser.get(link)
    time.sleep(30)
    button = browser.find_element_by_class_name (".btn.btn-lg.btn-primary.btn-add-to-basket")
    button.click()
#def solve_quiz_and_get_code():
    alert = browser.switch_to.alert
    x = alert.text.split(" ")[2]
    answer = str(math.log(abs((12 * math.sin(float(x))))))
    alert.send_keys(answer)
    alert.accept()
    try:
        alert = browser.switch_to.alert
        alert_text = alert.text
        print(f"Your code: {alert_text}")
        alert.accept()
    except NoAlertPresentException:
        print("No second alert presented")