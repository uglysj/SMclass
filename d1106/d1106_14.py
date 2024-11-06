import requests
from bs4 import BeautifulSoup

movie = {}
movie['제목'] = []
movie['관객수'] = []
movie['날짜'] = []

headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36", 'Accept-Language' : 'ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7'}
# for i in range(2020, 2024):
url = f'https://search.daum.net/search?w=tot&q=2023%EB%85%84%EC%98%81%ED%99%94%EC%88%9C%EC%9C%84&DA=MOR&rtmaxcoll=MOR'
res = requests.get(url, headers=headers)
res.raise_for_status()

soup = BeautifulSoup(res.text, 'lxml')
data = soup.select_one('#mor_history_id_0')
print(data)
img_urls = data.select('c-thumb')
print(img_urls[0][0])
  # titles = data.select('c-title')
  # for i in range(10):
  #   with open(f'd1106/images/{titles[i]}.jpg', 'wb') as f:
  #     get_img = requests.get(img_urls[i])
  #     f.write(get_img.content)
#   contents = data.select('c-contents-desc')
#   dates = data.select('c-contents-desc-sub')
#   for i in range(10):
#     movie['제목'].append(titles[i].next.strip())
#     movie['관객수'].append(int(contents[i].next.strip().replace(',','')[3:-2]))
#     movie['날짜'].append(dates[i].next.strip())

# print(movie)