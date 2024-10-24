import time
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import pyautogui

# url = 'https://new.land.naver.com/complexes?ms=37.4592802,126.8930386,17&a=APT:PRE:ABYG:JGC&e=RETAIL'
# browser = webdriver.Chrome()
# browser.maximize_window()
# browser.get(url)

# pyautogui.moveTo(1270, 550)
# time.sleep(1)
# pyautogui.moveTo(1270, 480)
# pyautogui.click()
# time.sleep(1)
# pyautogui.moveTo(200, 750)
# time.sleep(1)

# prev_height = browser.execute_script('return articleListArea.scrollHeight')
# print('화면 높이 :', prev_height)
# while True:
#   # browser.execute_script('window.scrollTo(0, articleListArea.scrollHeight)')
#   pyautogui.scroll(-prev_height)
#   time.sleep(2)
#   curr_height = browser.execute_script('return articleListArea.scrollHeight')
#   if prev_height == curr_height: break
#   prev_height = curr_height

# # all_height = browser.execute_script('return document.body.scrollHeight')
# # print('화면 전체높이 :', all_height)

# soup = BeautifulSoup(browser.page_source, 'lxml')
# data = soup.select_one('#complexOverviewList > div.list_contents > div.item_area > div')
# with open('c1024/naver_land.html', 'w+', encoding='UTF-8') as f:
#   f.write(soup.prettify())

# input('엔터키 입력완료')

# 매매가격이 낮은 5개, 전세가격이 낮은 5개를 출력하시오.
def price_chg(price):
  f_num = int(price[:price.find('억')]) * 100000000
  if price[price.find('억') + 1:] != '':
    s_num = int(price[price.find('억') + 1:]) * 10000
  else: s_num = 0
  result = f_num + s_num
  return result

def spec_chg(spec):
  sp_div = spec[0].split('/')
  return int(sp_div[1][:-2])

def ranking(land_info):
  if len(land_info) < 5:
    for i in range(len(land_info)):
      print(f'[ {land_info[i][3]}m² ]')
      print(f'{i + 1}.')
      print('단지명 :', land_info[i][1])
      print('거래방식 :', land_info[i][2])
      print('평수 :', land_info[i][3])
      print('가격 : {:,}'.format(land_info[i][4])); print('-' * 50)
  else:
    for i in range(5):
      print(f'[ {land_info[i][3]}m² ]')
      print(f'{i + 1}.')
      print('단지명 :', land_info[i][1])
      print('거래방식 :', land_info[i][2])
      print('평수 :', land_info[i][3])
      print('가격 : {:,}'.format(land_info[i][4])); print('-' * 50)

with open('c1024/naver_land.html', 'r+', encoding='UTF-8') as f:
  soup = BeautifulSoup(f, 'lxml')
data = soup.select_one('#articleListArea')
items = data.select('div.item')
m_list = []; j_list = []
for idx, item in enumerate(items):
  house = item.select_one('span.text').text.strip()
  type = item.select_one('span.type').text.strip()
  price = item.select_one('span.price').text.strip().replace(',', '').replace(' ', '')
  spec = item.select_one('span.spec').text.strip().split(',')
  if type == '전세':
    j_list.append([idx + 1, house, type, spec_chg(spec), price_chg(price)])
  elif type == '매매':
    m_list.append([idx + 1, house, type, spec_chg(spec), price_chg(price)])

# print('[ 전세 가격 낮은 순위 top5 ]\n')
# j_list.sort(key=lambda x: x[4])
# ranking(j_list)
j_list59 = [x for x in j_list if x[3] == 59]
j_list59.sort(key=lambda x: x[4])
ranking(j_list59)
j_list72 = [x for x in j_list if x[3] == 72]
j_list72.sort(key=lambda x: x[4])
ranking(j_list72)
j_list84 = [x for x in j_list if x[3] == 84]
j_list84.sort(key=lambda x: x[4])
ranking(j_list84)
j_list101 = [x for x in j_list if x[3] == 101]
j_list101.sort(key=lambda x: x[4])
ranking(j_list101)

# print('[ 매매 가격 낮은 순위 top5 ]\n')
# m_list.sort(key=lambda x: x[4])
# ranking(m_list)
m_list59 = [x for x in m_list if x[3] == 59]
m_list59.sort(key=lambda x: x[4])
ranking(m_list59)
m_list72 = [x for x in m_list if x[3] == 72]
m_list72.sort(key=lambda x: x[4])
ranking(m_list72)
m_list84 = [x for x in m_list if x[3] == 84]
m_list84.sort(key=lambda x: x[4])
ranking(m_list84)
m_list101 = [x for x in m_list if x[3] == 101]
m_list101.sort(key=lambda x: x[4])
ranking(m_list101)