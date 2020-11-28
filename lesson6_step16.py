from selenium import webdriver
import time
import os

current_dir = os.path.abspath(os.path.dirname(__file__))   
file_path = os.path.join(current_dir, 'file.txt')         
br = webdriver.Chrome()
link = 'http://suninjuly.github.io/file_input.html'
try:
    br.get(link)
    br.find_element_by_css_selector('#file').send_keys(file_path)
    br.find_element_by_css_selector('input[name="firstname"]').send_keys('Gena')
    br.find_element_by_css_selector('input[name="lastname"]').send_keys('Bars')
    br.find_element_by_css_selector('input[name="email"]').send_keys('gena-bars@ya.ru')
    br.find_element_by_css_selector('button[type="submit"]').click()
    answer = br.switch_to.alert.text
    print(answer.split()[-1])
finally:
    time.sleep(10)
    br.quit()