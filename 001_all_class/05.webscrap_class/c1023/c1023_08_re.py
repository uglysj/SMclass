import time, random, requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

url = 'https://flight.naver.com/'
browser = webdriver.Chrome()
browser.maximize_window() # 창 최대화
browser.get(url)

# 1. 출발지 선택
browser.find_element(By.CLASS_NAME, 'start').click()
time.sleep(1)
browser.find_element(By.CLASS_NAME, 'autocomplete_input__qbYlb').send_keys('김포')
time.sleep(1)
browser.find_element(By.XPATH, '//*[@id="__next"]/div/main/div[8]/div[2]/section/ul/li[2]/a/b/span[1]').click()
# browser.find_element(By.CLASS_NAME, 'searchResults_anchor__OXs_5').click()

# 2. 도착지 선택
browser.find_element(By.CLASS_NAME, 'end').click()
browser.find_element(By.CLASS_NAME, 'autocomplete_input__qbYlb').send_keys('제주')
time.sleep(2)
browser.find_element(By.XPATH, '//*[@id="__next"]/div/main/div[8]/div[2]/section/ul/li/a').click()

# 3. 가는날 선택
browser.find_element(By.CLASS_NAME, 'select_Date__Potbp').click(); time.sleep(2)
browser.find_element(By.XPATH, '//*[@id="__next"]/div/main/div[8]/div[2]/div[1]/div[2]/div/div[3]/table/tbody/tr[2]/td[4]/button').click()

# 4. 오는날 선택
browser.find_element(By.XPATH, '//*[@id="__next"]/div/main/div[2]/div/div/div[2]/div[2]/button[2]').click(); time.sleep(2)
browser.find_element(By.XPATH, '//*[@id="__next"]/div/main/div[8]/div[2]/div[1]/div[2]/div/div[3]/table/tbody/tr[2]/td[7]/button').click()

# 5. 인원수 선택
browser.find_element(By.XPATH, '//*[@id="__next"]/div/main/div[2]/div/div/div[2]/div[3]/button').click(); time.sleep(2)
browser.find_element(By.XPATH, '//*[@id="__next"]/div/main/div[2]/div/div/div[2]/div[4]/div/div/div[1]/div[1]/button[2]').click()

# 6. 항공권 검색
browser.find_element(By.XPATH, '//*[@id="__next"]/div/main/div[2]/div/div/div[2]/button[1]').click()
time.sleep(2)
browser.find_element(By.XPATH, '//*[@id="__next"]/div/main/div[2]/div/div/div[2]/button[1]').click()

# 7. 데이터를 검색하는 동안 대기 상태
# 검색 중
time.sleep(10)
# -------------------------------------
# 화면 대기 함수
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC

# 화면 대기 - 30초 동안 대기
# 화면에 찾으려고 하는 <html>요소가 있는지 확인
# elem = WebDriverWait(browser, 120).until(lambda x: x.find_element(By.XPATH,'//*[@id="__next"]/div/main/div[4]/div/div[2]'))

# 화면 스크롤 내리기
# 현재 스크롤 높이 검색 - 1000
prev_height = browser.execute_script('return document.body.scrollHeight')
print('최초 높이 :', prev_height)

# 스크롤 내리기 - 1000
while True:
  browser.execute_script('window.scrollTo(0, document.body.scrollHeight)')
  time.sleep(2) # 다른 정보가 추가될 때까지
  # 높이 확인 - 2000
  curr_height = browser.execute_script('return document.body.scrollHeight')
  if prev_height == curr_height:
    break
  prev_height = curr_height
  print('현재 높이 :', curr_height)

# 데이터 가져와서 처리
# BeautifulSoup 데이터 처리
# 웹 스크래핑
soup = BeautifulSoup(browser.page_source, 'lxml')
with open('c1023/flight.html', 'w+', encoding='UTF-8') as f:
  f.write(soup.prettify())

input('enter키를 입력하면 프로그램이 중료됩니다.')
browser.quit()

# 완료
time.sleep(100)