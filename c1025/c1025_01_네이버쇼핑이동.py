import time, csv
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# https://www.naver.com
# 네이버 쇼핑 검색창 입력 enter키 입력
# 네이버 쇼핑 클릭
# 네이버 쇼핑에서 무선 마우스 검색창 입력 enter키 입력

url = 'https://www.naver.com'
browser = webdriver.Chrome()
browser.maximize_window()
browser.get(url)

browser.find_element(By.XPATH, '//*[@id="query"]').send_keys('네이버 쇼핑', Keys.ENTER)
time.sleep(2)
browser.find_element(By.XPATH, '//*[@id="main_pack"]/section[1]/div/div/div[1]/div/div[2]/a').click()
time.sleep(2)
browser.switch_to.window(browser.window_handles[1])
browser.find_element(By.XPATH, '//*[@id="gnb-gnb"]/div[2]/div/div[2]/div/div[2]/form/div[1]/div/input').send_keys('무선 마우스', Keys.ENTER)
time.sleep(2)