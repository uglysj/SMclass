import requests
from bs4 import BeautifulSoup

url = "https://www.coupang.com/np/search?q=%EB%85%B8%ED%8A%B8%EB%B6%81&channel=user&component=&eventCategory=SRP&trcid=&traid=&sorter=scoreDesc&minPrice=&maxPrice=&priceRange=&filterType=&listSize=36&filter=&isPriceRange=false&brand=&offerCondition=&rating=0&page=1&rocketAll=false&searchIndexingToken=1=9&backgroundColor="
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36", 'Accept-Language' : 'ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7'}
res = requests.get(url,headers=headers)
res.raise_for_status() # 에러시 종료

# 제목, 금액, 평점, 평가수
soup = BeautifulSoup(res.text,"lxml")
# data = soup.select_one('ul#productList')
# lists = data.select('li')
# print('1. 링크주소 :', 'https://www.coupang.com' + lists[0].select_one('a')['href'])
# print('2. 제목 :', lists[0].select_one('div.name').text)
# print('3. 금액 :', int(lists[0].select_one('strong.price-value').text.replace(',', '')))
# print('4. 평점 :', float(lists[0].select_one('em.rating').text))
# print('5. 평가수 :', int(lists[0].select_one('span.rating-total-count').text[1:-1]))
# print('6. 이미지주소 :', 'https:' + lists[0].select_one('img')['src'])

lists = soup.select('#productList > li')
n_lists = []
for idx, list in enumerate(lists):
  try:
    price = int(list.select_one('strong.price-value').text.replace(',', ''))
    rating = float(list.select_one('em.rating').text)
    count = int(list.select_one('span.rating-total-count').text[1:-1])
    link = 'https://www.coupang.com' + list.select_one('a')['href']
    title = list.select_one('div.name').text
    img_src = 'https:' + list.select_one('img')['src']
    if price >= 900000 and rating >= 4.5 and count >= 500:
      print(f'[ {idx + 1} 번째 ]')
      print('1. 링크주소 :', link)
      print('2. 제목 :', title)
      print('3. 금액 :', price)
      print('4. 평점 :', rating)
      print('5. 평가수 :', count)
      print('6. 이미지주소 :', img_src)
      n_lists.append([title, price, rating, count, link, img_src])
    else:
      print(f'[ {idx + 1} 번째 ] : 제외')
  except Exception as e:
    print(f'[ {idx + 1} ]: 에러')
    pass

while True:
  print(); print('[ 노트북 비교 ]')
  print('-' * 50)
  print('1. 금액 오름차순')
  print('2. 금액 내림차순')
  print('3. 평가수 오름차순')
  print('4. 평가수 내림차순')
  print('0. 종료')
  print('-' * 50)
  choice = input("원하는 번호를 입력하세요.>> ")

  if choice == '1':
    n_lists.sort(key=lambda x: x[1])
  elif choice == '2':
    n_lists.sort(key=lambda x: x[1], reverse=True)
  elif choice == '3':
    n_lists.sort(key=lambda x: x[3])
  elif choice == '4':
    n_lists.sort(key=lambda x: x[3], reverse=True)
  elif choice == '0':
    print("프로그램 종료")
    break
  print(n_lists)