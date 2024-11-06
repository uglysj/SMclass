import requests
from bs4 import BeautifulSoup

url = 'https://news.naver.com/main/ranking/popularDay.naver'
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36'}
res = requests.get(url, headers=headers)
res.raise_for_status()

soup = BeautifulSoup(res.text, 'lxml')
boxs = soup.find('div', {'class': 'rankingnews_box_wrap'}).find_all('div', {'class': 'rankingnews_box'})
for idx, b in enumerate(boxs):
  print(f"{idx + 1}. 타이틀 :", b.find('strong', {'class': 'rankingnews_name'}).text); print('-' * 70)
  list = b.find('ul', {'class': 'rankingnews_list'})
  titles = list.find_all('li')
  for idx, t in enumerate(titles):
    print(f"{idx + 1} :", t.find('a').text)
  print('-' * 70); print()