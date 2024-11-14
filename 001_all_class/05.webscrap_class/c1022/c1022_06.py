import requests
from bs4 import BeautifulSoup

url = 'https://www.melon.com/chart/index.htm'
header = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36'}
res = requests.get(url, headers=header)
res.raise_for_status() # 에러 시 종료

soup = BeautifulSoup(res.text, 'lxml')
# 순위, 사진링크주소, 제목, 가수명
data = soup.select_one('#frm > div > table')
tops = data.select('tr')

title = []
tits = tops[0].select('th')
for idx, tit in enumerate(tits):
  if idx == 0 or idx == 2 or idx == 4: continue
  title.append(tit.text.strip())

for i in range(1, 101):
  conts = tops[i].select('td')
  print("순위 :", conts[1].select_one('span.rank').text)
  print("이미지주소 :", conts[3].select_one('img')['src'])
  print("제목 :", conts[5].select_one('span > a').text)
  print('가수명 :', conts[5].select_one('div.rank02 > a').text + '\n')