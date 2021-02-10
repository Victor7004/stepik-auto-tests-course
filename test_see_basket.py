from pages.product_page import ByPage
from pages.login_page import LoginPage
from pages.locators import BasketPageLocators
from pages.basket_page import BasketPage
from selenium import webdriver
from selenium.webdriver.common.by import By
import faker
import pytest
import time

#@pytest.mark.need_review
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ByPage(browser, link)
    page.open()
    page.go_to_basket_page()
    page.should_be_in_element_present()
    page.is_not_basket_empty()
