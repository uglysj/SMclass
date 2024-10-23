import time, requests, random
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

url = 'https://www.naver.com'

# 크롬브라우저열기
browser = webdriver.Chrome()
# 네이버 페이지 이동
browser.get(url)
# 로그인버튼 선택
elem = browser.find_element(By.CLASS_NAME, 'MyView-module__link_login___HpHMW')
# 로그인버튼 클릭
elem.click()
time.sleep(random.randint(2, 5))

# 자바스크립트 호출방법
id = 'sjlee_0220'
pw = ''
input_js = f'document.getElementById("id").value = "{id}"; document.getElementById("pw").value = "{pw}";'
browser.execute_script(input_js)
time.sleep(random.randint(2, 5))
# 로그인 버튼 클릭
elem = browser.find_element(By.ID, 'log.login')
elem.click()

# 완료
time.sleep(100)
# ------------------------------------------
# # id 값을 입력
# elem = browser.find_element(By.ID, 'id')
# elem.send_keys('')
# time.sleep(random.randint(2, 5))
# # pw 값을 입력
# elem = browser.find_element(By.ID, 'pw')
# elem.send_keys('')
# time.sleep(random.randint(2, 5))
# # 로그인 버튼 클릭
# elem = browser.find_element(By.ID, 'log.login')
# elem.click()