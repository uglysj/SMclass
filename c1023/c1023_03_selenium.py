# pip install selenium / chrome 드라이버 설치 필요
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import requests
from bs4 import BeautifulSoup

# Chrome() - ()안에 chromedriver.exe 위치 지점을 입력해줘야 함.
# root에 파일이 저장되어 있으면 입력하지 않아도 됨.
browser = webdriver.Chrome()
browser.get('https://www.naver.com')

# html 위치 찾기 - requests: select
elem = browser.find_element(By.CLASS_NAME, 'MyView-module__link_login___HpHMW')

elem.click() # 클릭
browser.back() # 뒤로가기
browser.forward() # 앞으로가기
browser.refresh() # 새로고침

elem = browser.find_element(By.NAME, 'pw')
elem = browser.find_element(By.ID, 'query')

# 글자입력
elem.send_keys('네이버 영화')
# enter 키 입력
elem.send_keys(Keys.ENTER)
# 새창 이동
browser.switch_to.window(browser.window_handles[1])

time.sleep(100)