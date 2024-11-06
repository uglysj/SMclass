import requests
from bs4 import BeautifulSoup

url = 'https://news.naver.com/main/ranking/popularDay.naver'
header = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36'}
res = requests.get(url, headers=header)
res.raise_for_status() # 에러 시 종료

# 태그를 활용한 검색방법
# find, find_all, select_one, select

soup = BeautifulSoup(res.text, 'lxml')
# print(soup.find('h2', {'class': 'rankingnews_tit'}))
# print(soup.select_one('h2.rankingnews_tit').text)
# print(soup.select_one('div#header'))

# select_one, select 사용
wrap = soup.select_one('div.rankingnews_box_wrap')
boxs = wrap.select('div.rankingnews_box')
for idx, b in enumerate(boxs):
  print(f'[ {b.select_one('strong').text} ]')
  ranking_lists = b.select('ul.rankingnews_list>li')
  for idx, t in enumerate(ranking_lists):
    print(f'{idx + 1}. {t.select_one('div.list_content>a').text}')
  print()