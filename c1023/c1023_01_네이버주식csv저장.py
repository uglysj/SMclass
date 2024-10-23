import requests, os, time, csv
from bs4 import BeautifulSoup

url = "https://finance.naver.com/sise/lastsearch2.naver"
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36", 'Accept-Language' : 'ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7'}
res = requests.get(url,headers=headers)
res.raise_for_status() # 에러시 종료

soup = BeautifulSoup(res.text,"lxml")

# 기준점
data = soup.select_one('#contentarea > div.box_type_l > table')
stocks = data.select('tr')

# 상단 타이틀 - csv파일로 저장
f = open('c1023/stock.csv', 'w+', encoding='UTf-8-sig', newline='')
writer = csv.writer(f)
st_list = [st.text for st in stocks[0].select('th')]
writer.writerow(st_list) # writerow 리스트 타입을 저장

# 값 불러오기
for stock in stocks:
  sts = stock.select('td')
  if len(sts) <= 1: continue
  sto_list = [st.text.replace('\n', '').replace('\t', '') for st in sts]
  writer.writerow(sto_list)
f.close()

print('완료')