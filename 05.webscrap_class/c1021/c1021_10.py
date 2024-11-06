import requests
from bs4 import BeautifulSoup

url = 'https://search.daum.net/search?w=tot&q=%EC%98%81%ED%99%94%EC%88%9C%EC%9C%84&DA=MOR&rtmaxcoll=MOR'
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36'}
res = requests.get(url, headers=headers)
res.raise_for_status()

soup = BeautifulSoup(res.text, 'lxml')
data = soup.find('c-flicking', {'id': 'mor_history_id_0'})
screens = data.find_all('c-doc')
# print('개수 :', len(screens))
for idx, screen in enumerate(screens):
  if idx == 10: break
  # title = screen.find('c-title').next.replace(" ", "")
  print("순위 :", screen.find('c-badge-text').next)
  print("제목 :", screen.find('c-title').next)
  print("예매율 :", screen.find('c-contents-desc').next)
  print("날짜 :", screen.find('c-contents-desc-sub').next)
  print("이미지 url :", screen.find('c-thumb')['data-original-src'])
  with open(f'c1021/{idx+1}.jpg', 'wb') as f:
    re_img = requests.get(screen.find('c-thumb')['data-original-src'])
    f.write(re_img.content)
print('완료')