import requests
from bs4 import BeautifulSoup

url = 'https://finance.naver.com/sise/lastsearch2.naver'
header = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36'}
res = requests.get(url, headers=header)
res.raise_for_status() # 에러 시 종료

soup = BeautifulSoup(res.text, 'lxml')
box = soup.select_one('div.box_type_l')

titles = box.select('tr.type1 > th')
for idx, title in enumerate(titles):
  print(title.text, end='\t')
print(); print('-' * 100)

no_datas = box.select('tr > td.no')
t_datas = box.select('tr > td > a.tltle')
n_datas = box.select('tr > td.number')
for i, data in enumerate(n_datas):
  print(i, data.text.strip())
# for i in range(30):
#   print(no_datas[i].text, end='\t')
#   print(t_datas[i].text)

# print(len(n_datas))