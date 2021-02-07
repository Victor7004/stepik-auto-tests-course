import pytest
from selenium import webdriver
import time
import math

#final = "" 

@pytest.fixture(scope="function")
def browser():
    print("\nstart dr for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit dr..")
    browser.quit()
    #print("\nAnswer: " + final) 
    
lincs = [
    "https://stepik.org/lesson/236895/step/1",
    "https://stepik.org/lesson/236896/step/1",
    "https://stepik.org/lesson/236897/step/1",
    "https://stepik.org/lesson/236898/step/1",
    "https://stepik.org/lesson/236899/step/1",
    "https://stepik.org/lesson/236903/step/1",
    "https://stepik.org/lesson/236904/step/1",
    "https://stepik.org/lesson/236905/step/1"  
   ]

@pytest.mark.parametrize('linc', lincs)
def test_guest_should_see_login_link(browser, linc):
    link = linc
    browser.get(link)
    browser.implicitly_wait(10) 
    text_area = browser.find_element_by_css_selector(".textarea")
    text_area.send_keys(str(math.log(int(time.time()))))
    button = browser.find_element_by_css_selector (".submit-submission ")
    button.click()
    result = browser.find_element_by_class_name('smart-hints__hint').text
    assert "Correct" in result
    #try:
        #assert result == 'Correct!' 
    #except AssertionError:
        #final += result
    