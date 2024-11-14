import requests
from bs4 import BeautifulSoup

url = 'https://www.google.co.kr'
header = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36'}
res = requests.get(url, headers=header)
res.raise_for_status() # 에러 시 종료

soup = BeautifulSoup(res.text, 'lxml')

# title
# print(soup.select_one('title'))
# print(soup.select_one('body > div.L3eUgb > div.o3j99.LLD4me.yr19Zb.LS8OJ > div > img'))
print(soup.select_one('div.L3eUgb'))
data = soup.select_one('div.L3eUgb')
lists = data.select('div.o3j99')
print('개수 :', len(lists))
for list in lists:
  print(list.select_one('style'))