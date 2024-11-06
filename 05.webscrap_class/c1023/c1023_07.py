import time, random
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

url = 'https://www.daum.net'
browser = webdriver.Chrome()
browser.get(url)

elem = browser.find_element(By.CLASS_NAME, 'btn_login')
elem.click()
time.sleep(random.randint(2, 4))

id = 'aaa'
pw = '1111'
input_js = f'document.getElementById("loginId--1").value = "{id}"; document.getElementById("password--2").value = "{pw}";'
browser.execute_script(input_js)
time.sleep(random.randint(2, 4))

elem = browser.find_element(By.CLASS_NAME, 'submit')
elem.click()

time.sleep(100)