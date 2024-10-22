import requests
from bs4 import BeautifulSoup

url = 'https://finance.naver.com/'
header = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36'}
res = requests.get(url, headers=header)
res.raise_for_status() # 에러 시 종료

soup = BeautifulSoup(res.text, 'lxml')

aside_popular = soup.select_one('div.aside_popular')
print(f'[ {aside_popular.select_one('span').text} ]')
pops = aside_popular.select('tbody>tr')
sum = 0
for i, pop in enumerate(pops):
  # next_sibling : 형제관계, find_next_sibling : 형제관계 중 검색
  print('회사명 :', pop.select_one('a').text)
  print('현재가 :', pop.select_one('td').text)
  sum += int(pop.select_one('td').text.replace(',',""))
  # print('변동 :', pop.select_one('td').find_next_sibling('td').select_one('span').text)
  # print('변동액 :', pop.select_one('td').find_next_sibling('td').select_one('span').next.next.next.strip())
  sps = pop.select_one('td').find_next_sibling('td').select('span')
  tit = ['변동', '변동액']
  for idx, sp in enumerate(sps):
    print(tit[idx], ":", sp.text.strip())
  print('-' * 50)
print(f'합계 : {sum:,}')