import requests
from bs4 import BeautifulSoup

url = 'https://news.naver.com/main/ranking/popularDay.naver'
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36'}
res = requests.get(url, headers=headers)
res.raise_for_status()

# html 전체를 가져옴.
soup = BeautifulSoup(res.text, 'lxml')
wrap = soup.find('div', {'class': 'rankingnews_box_wrap'})
boxs = wrap.find_all('div', {'class': 'rankingnews_box'})
with open('c1021/news.txt', 'w', encoding='UTF-8') as f:
  for idx, b in enumerate(boxs):
    # print(f"[ {idx + 1}. 언론사 : {b.find('strong', {'class': 'rankingnews_name'}).text} ]")
    f.write(f"[ {idx + 1}. 언론사 : {b.find('strong', {'class': 'rankingnews_name'}).text} ]\n")
    list = b.find('ul', {'class': 'rankingnews_list'})
    con_titles = list.find_all('li')
    for idx, t in enumerate(con_titles):
      # print(idx + 1, ":", t.find('a').text)
      f.write(f"{idx + 1} : {t.find('a').text}\n")