import requests
from bs4 import BeautifulSoup

url = 'https://www.11st.co.kr/browsing/BestSeller.tmall?method=getBestSellerMain&xfrom=main^gnb'
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36'}
res = requests.get(url, headers=headers)
res.raise_for_status()

soup = BeautifulSoup(res.text, 'lxml')
B_lists = soup.find('div', {'id': 'bestPrdList'}).find('ul', {'class': 'cfix'}).find_all('li')
for i, title in enumerate(B_lists):
  p_title = title.find('div', {'class': 'pname'}).p.text
  p_price = title.find('strong', {'class': 'sale_price'}).text
  print(f"{i + 1}. {p_title} / 금액 : {p_price} 원")