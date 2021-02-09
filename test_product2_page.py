from pages.product_page import ByPage
from pages.locators import ByPageLocators
from pages.login_page import LoginPage
import faker
import pytest
import time
import math


class TestUserAddToBasketFromProductPage():

  
    #@pytest.fixture(scope="function", autouse=True)
    def setup(self,browser):
        login_link= "http://selenium1py.pythonanywhere.com/ru/accounts/login/"
        page = LoginPage(browser, login_link)
        page.open()
        f = faker.Faker()
        email = f.email()
        password = str(time.time())
        page.register_new_user(email=email,password=password)
        page.should_be_authorized_user()

    #@pytest.mark.need_review
    def test_user_can_add_product_to_basket(browser):
        link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/coders-at-work_207/?promo=offer1"
        page = ByPage(browser, link)
        page.open()
        page.user_can_add_product_to_basket()


    def test_user_cant_see_success_message(browser):
        link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/coders-at-work_207/?promo=offer1"
        page = ByPage(browser, link)
        page.open()
        page.user_cant_see_success_message() 