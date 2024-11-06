import time, requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# for i in range(1, 6):
#   url = f'https://www.yeogi.com/domestic-accommodations?keyword=%EA%B0%95%EB%A6%89&autoKeyword=&checkIn=2024-10-23&checkOut=2024-10-24&personal=2&freeForm=true&page={i}'
#   brower = webdriver.Chrome()
#   # 이동하려는 주소 입력
#   brower.get(url)
#   time.sleep(5)
#   soup = BeautifulSoup(brower.page_source, 'lxml')
#   # 파일 저장
#   with open(f'c1023/yeogi_sel{i}.html', 'w+', encoding='UTF-8') as f:
#     f.write(soup.prettify())

# 파일 불러오기 - BeautifulSoup 으로 파싱
for i in range(5):
  with open(f'c1023/yeogi_sel{i + 1}.html', 'r+', encoding='UTF-8') as f:
    soup = BeautifulSoup(f, 'lxml')
  data = soup.select_one('#__next > div > main > section > div.css-1qumol3')
  lists = data.select('a')
  print('[ 강릉 숙소 ]')
  print(f'[ {i + 1}번째 페이지 ]')
  for idx, list in enumerate(lists):
    try:
      rating = float(list.select_one('span.css-9ml4lz').text.strip())
      count = int(list.select_one('span.css-oj6onp').text.strip()[:-4].replace(',',''))
      price = int(list.select_one('span.css-5r5920').text.strip().replace(',',''))
      # img = list.select_one('div.css-nl3cnv > img')['src']
      if count >= 500 and rating >= 9.0 and price <= 120000:
        print(f'{(i * 20) + idx + 1}.')
        print('주소 :', 'https://www.yeogi.com' + list['href'])
        print('호텔명 :', list.select_one('.css-8fn780 > h3').text.strip())
        print('평점 :', rating)
        print('평가수 :', count)
        print('가격 :', price)
        # print('이미지주소 :', img)
        print('-' * 50)
      else:
        print(f'{(i * 20) + idx + 1}. 조건미달'); print('-' * 50)
        continue
    except Exception as e:
      print(f'{(i * 20) + idx + 1}. 에러', e); print('-' * 50)
      pass

# time.sleep(100)

# requests로 정보 가져오기
# url = 'https://www.yeogi.com/domestic-accommodations?keyword=%EA%B0%95%EB%A6%89&autoKeyword=&checkIn=2024-10-23&checkOut=2024-10-24&personal=2&freeForm=true'
# headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36", 'Accept-Language': 'ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7'}
# res = requests.get(url, headers=headers)
# res.raise_for_status()
# soup = BeautifulSoup(res.text, 'lxml')

# with open('c1023/yeogi.html', 'w+', encoding='UTF-8') as f:
#   f.write(soup.prettify())

# data = soup.select_one('#__next > div > main > section > div.css-1qumol3')
# print(data)