from .base_page import BasePage
from selenium.webdriver.common.by import By
from .locators import ByPageLocators
from .login_page import LoginPage
from .base_page import BasePage
from .locators import ByPageLocators
from pages.locators import BasketPageLocators
from selenium import webdriver
#from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import pytest

class ByPage(BasePage):
    def go_to_button_page(self):
        button = self.browser.find_element(*ByPageLocators.BUTTON_LINK)
        button.click()

    def add_to_cart_page(self):
        add_btn = self.browser.find_element(*ByPageLocators.ADD_TO_CART)
        add_btn.click()         

    def should_be_by_busket(self):
        self.should_be_by_book()
        self.should_be_by_price()

    def compare_name(self):
        alert_name = self.browser.find_elements(*ByPageLocators.ALERT_LIST)[0].text
        name = self.browser.find_element(*ByPageLocators.BOOK_FORM).text
        assert alert_name == name, "The name in the basket does not match"

    def compare_price(self):
        alert_price = self.browser.find_elements(*ByPageLocators.ALERT_LIST)[2].text
        price = self.browser.find_element(*ByPageLocators.PRICE_FORM).text
        assert alert_price == price, "The price in the basket does not match"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), "Success message is presented, but should not be" 
   
    def element_should_disappear(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), "Element doesn't disappear" 

    def user_cant_see_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), "Success message is presented, but should not be"

    def user_can_add_product_to_basket(self): 
        self.compare_name()
        self.compare_price() 
        
    def go_to_basket_page(self):
        button = self.browser.find_element(*BasketPageLocators.BUTTON_ITEM)
        button.click() 
    
    def should_be_in_element_present(self):
        #assert self.is_element_present(*BasePageLocators.LOGIN_LINK), "Login link is not presented"
        #assert 'empty' in self.browser.find_element(By.XPATH, "//p[contains(text(), 'empty')]"), " Basket not empty"
        #assert 'empty' in self.browser.find_element_by_xpyth( "//p[contains(text(), 'empty')]"), " Basket not empty"                       
        assert 'empty' in self.browser.find_element(By.CSS_SELECTOR, 'p').text

    def is_not_basket_empty(self):
         assert self.is_not_element_present(*BasketPageLocators.BASKET_ITEM), "Basket is not empty"















