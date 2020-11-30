from selenium import webdriver
import os
import time

with open('test.txt', 'w') as file:
        file.write('test1 for mls 228')
pth = os.path.abspath("test.txt")


link = " http://suninjuly.github.io/file_input.html" 

browser = webdriver.Chrome()
browser.get(link)



try:
   

    input1 = browser.find_element_by_tag_name('input')
    input1.send_keys("Ivan")
    input2 = browser.find_element_by_name('lastname')
    input2.send_keys("Petrov")
    input3 = browser.find_element_by_name('email')
    input3.send_keys("S@.ia")

    input4 = browser.find_element_by_id('file')
    input4.send_keys(pth) 
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

finally:
    # 
    time.sleep(60)
    # 
    browser.quit()