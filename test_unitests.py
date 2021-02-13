from selenium import webdriver
import unittest
import time


class TestClass(unittest.TestCase):


    def setUp(self):
        self.browser = webdriver.Chrome()

    def test_class_name(self):
        browser = self.browser
        link = "http://suninjuly.github.io/registration1.html"
        browser.get(link)

        # 
        input1 = browser.find_element_by_class_name('first')
        input1.send_keys("Ivan")
        input2 = browser.find_element_by_class_name('second')
        input2.send_keys("Petrov")
        input3 = browser.find_element_by_class_name('third')
        input3.send_keys("Smolensk")

        elements = list(filter(lambda el : el.get_attribute("required"), browser.find_elements_by_css_selector('input')))

        self.assertEqual(test_class_name(3),len(elements), "Should be absolute value of a number")
        #
        button = browser.find_element_by_css_selector("button.btn")
        button.click()

        # 
        # 
        time.sleep(1)

        # 
        welcome_text_elt = browser.find_element_by_tag_name("h1")
        # 
        welcome_text = welcome_text_elt.text

    def tearDown(self):
        self.browser.close()

    def setUp(self):
        self.browser = webdriver.Chrome()


    def test_class_name(self):
        browser = self.browser
        link = "http://suninjuly.github.io/registration2.html"
        browser.get(link)

        # 
        input1 = browser.find_element_by_class_name('first')
        input1.send_keys("Ivan")
        input2 = browser.find_element_by_class_name('second')
        input2.send_keys("Petrov")
        input3 = browser.find_element_by_class_name('third')
        input3.send_keys("Smolensk")

        elements = list(filter(lambda el : el.get_attribute("required"), browser.find_elements_by_css_selector('input')))

        self.assertEqual(test_class_name(3),len(elements) , "Should be absolute value of a number")
        #
        button = browser.find_element_by_css_selector("button.btn")
        button.click()

        # 
        # 
        time.sleep(1)

        # 
        welcome_text_elt = browser.find_element_by_tag_name("h1")
        # 
        welcome_text = welcome_text_elt.text


    def tearDown(self):
        self.browser.close()
        


if __name__ == "__main__":
    unittest.main()