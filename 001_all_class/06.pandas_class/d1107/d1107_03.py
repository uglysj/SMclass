from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

c = open('d1107/screen.csv', 'a', encoding='utf-8')
c.write('제목,관객수,날짜\n') # 1번만 글저장

# 웹스크래핑 시작
for syear in range(2020, 2024):
  with open(f'd1107/screen{syear}.html', 'r+', encoding='utf-8') as f:
    soup = BeautifulSoup(f, 'lxml')
    print(f'{syear}년도 ------------------------')
    # 기준점
    data = soup.select_one('#mor_history_id_0 > div > div.flipsnap_view > div > div:nth-child(1) > c-flicking-item > c-layout > div > c-list-doc > ul')
    screens = data.select('li')
    for i, screen in enumerate(screens):
      print(f'{i+1}.')
      s_img = screen.select_one('div.wrap_thumb img')['src']
      title = screen.select_one('.tit-g').text.strip()
      number = int(screen.select_one('div.item-contents a').text.strip()[3:-2].replace(',', ''))
      sdate = screen.select_one('span.conts-subdesc').text.strip()[:-1]
      # s_list = [title,number,sdate]
      # 파일 저장
      c.write(f'{title},{number},{sdate}\n')
c.close()

print('프로그램 완료')

# a_list = ['서울의 봄',100,'2024-11-07']
# with open('d1107/s3.csv', 'w+', encoding='utf-8') as f:
#   f.write('제목,관객수,날짜\n')
#   for i in range(10):
#     f.write(f'{a_list[0]},{a_list[1]},{a_list[2]}\n')

# print('프로그램 완료')