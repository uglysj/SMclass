import time, random
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# url = 'https://www.yanolja.com/'
# browser = webdriver.Chrome()
# browser.maximize_window()
# browser.get(url)

# # 검색창 클릭
# browser.find_element(By.XPATH, '//*[@id="__next"]/div/div/header/section/a[2]').click()

# # 날짜 선택
# browser.find_element(By.XPATH, '//*[@id="__next"]/div/main/div/div[1]/form/div/div[2]/div[1]/button').click()
# time.sleep(2)
# # 체크인 11/11
# browser.find_element(By.XPATH, '/html/body/div[4]/div/div/section/section[3]/div/div/div/div[2]/div/div[2]/div[2]/div/table/tbody/tr[3]/td[2]').click()
# time.sleep(2)
# # 체크아웃 11/13
# browser.find_element(By.XPATH, '/html/body/div[4]/div/div/section/section[3]/div/div/div/div[2]/div/div[2]/div[2]/div/table/tbody/tr[3]/td[4]').click()
# time.sleep(2)
# # 확인버튼
# browser.find_element(By.XPATH, '/html/body/div[4]/div/div/section/section[4]/button').click()
# time.sleep(1)

# # 검색어 입력
# elem = browser.find_element(By.XPATH, '//*[@id="__next"]/div/main/div/div[1]/form/div/div[1]/div/input')
# elem.send_keys('강릉호텔', Keys.ENTER)

# # 자동 로딩 대기 - 화면의 호텔검색내용이 뜰때까지 최대 30초 대기
# WebDriverWait(browser, 30).until(lambda x: x.find_element(By.XPATH, '//*[@id="__next"]/div/main/section/div[2]'))
# # time.sleep(10)

# # 화면을 스크롤해서 내리기 반복
# # excute_script() : 자바 스크립트 실행함수
# prev_scroll = browser.execute_script('return document.body.scrollHeight')
# while True:
#   browser.execute_script('window.scrollTo(0, document.body.scrollHeight)')
#   time.sleep(1)
#   curr_scroll = browser.execute_script('return document.body.scrollHeight')
#   if prev_scroll == curr_scroll: break
#   prev_scroll = curr_scroll
# print("스크롤 내리기 완료")

# # 파일 저장하기
# soup = BeautifulSoup(browser.page_source, 'lxml')
# with open('c1024/yanolja.html', 'w+', encoding='UTF-8') as f:
#   f.write(soup.prettify())

# 파일 불러오기
with open('c1024/yanolja.html', 'r+', encoding='UTF-8') as f:
  soup = BeautifulSoup(f, 'lxml')

# 데이터 출력
data = soup.select_one('#__next > div > main > section > div.PlaceListBody_listContainer__2qFG1')
lists = data.select('div.PlaceListItemText_container__fUIgA')
cnt, fcnt, ecnt = 0, 0, 0
search_list = []
print('[ 강릉 호텔 ]')
for idx, list in enumerate(lists):
  try:
    hotel = list.select_one('strong.PlaceListTitle_text__2511B').text.strip()
    rating = float(list.select_one('span.PlaceListScore_rating__3Glxf').text.strip())
    price = int(list.select_one('span.PlacePriceInfoV2_discountPrice__1PuwK').text.strip().replace(',',''))
    
    if rating >= 4.8 and price <= 170000:
      print(f'{idx + 1}.')
      print('호텔명 :', hotel)
      print('평점 :', rating)
      print('금액 : {:,}'.format(price))
      print('-' * 50); cnt += 1
      search_list.append([idx + 1, hotel, rating, price])
    else:
      print(f"{idx + 1}. 조건미달"); print('-' * 50); fcnt += 1
  except Exception as e:
    print(f'{idx + 1}. 에러', e); print('-' * 50); ecnt += 1

print('[ 검색 정보 ]')
print('총 개수 :', len(lists))
print('1. 조건 맞는 개수 :', cnt)
print('2. 조건에 맞지 않는 개수 :', fcnt)
print('3. 예외처리 개수 :', ecnt)

# 리스트에 담고 정렬
# [1, 호텔명, 평점, 가격]
# 평점 역순정렬
# search_list.sort(key=lambda x: x[2], reverse=True)
# print(search_list[:5])

# 금액 순차정렬
search_list.sort(key=lambda x: x[3])
print(search_list[:5])

# input("Enter키를 입력하면 완료됩니다.")