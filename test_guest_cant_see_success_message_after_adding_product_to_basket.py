from pages.product_page import ByPage
import pytest
import math

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"
def test_guest_can_add_product_to_basket(browser, link):
    page = ByPage(browser, link)
    page.open()
    page.go_to_button_page()
    page.is_not_element_present()
    
  