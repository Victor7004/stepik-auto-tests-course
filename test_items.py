import pytest
from selenium import webdriver
import time 

def test_add_to_basket_button(browser):
    link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    browser.get(link)                                                                           
    time.sleep(30)
    button = len(browser.find_elements_by_css_selector("button.btn-add-to-basket"))
    assert button > 0, 'Button not found !!!'
    











