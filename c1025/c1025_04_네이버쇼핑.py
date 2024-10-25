import time, csv
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

with open('c1025/naver/shopping1.html', 'r+', encoding='UTF-8') as f:
  soup = BeautifulSoup(f, 'lxml')

# 기준점
data = soup.select_one('#content > div.style_content__xWg5l > div.basicList_list_basis__uNBZx')

# 광고 상품 4개
# pro_lists = data.select('div.adProduct_item__1zC9h')
# # csv 저장
# f = open('c1025/naver/nshop.csv', 'a', encoding='UTF-8-sig', newline='')
# writer = csv.writer(f)

# for i, pro_list in enumerate(pro_lists):
#   print(f'{i + 1}.')
#   try:
#     # 제목
#     title = pro_list.select_one('div.adProduct_info_area__dTSZf > div.adProduct_title__amInq > a').text.strip()
#     print('상품명 :', title)
#     # 가격
#     price = int(pro_list.select_one('div.adProduct_info_area__dTSZf > div.adProduct_price_area__yA7Ad > strong > span.price > span.price_num__S2p_v > em').text.strip().replace(',', ''))
#     print('가격 :', price)
#     # 평점
#     rating = float(pro_list.select_one('div.adProduct_etc_box__UJJ90 > span.adProduct_etc___brfw > a > span.adProduct_rating__PaMzh').text.strip())
#     print('평점 :', rating)
#     # 평가수
#     num = int(pro_list.select_one('div.adProduct_etc_box__UJJ90 > span.adProduct_etc___brfw > a > em').text.strip().replace(',', ''))
#     print('평가수 :', num)
#     # 찜
#     save = int(pro_list.select_one('div.adProduct_etc_box__UJJ90 > span.adProduct_etc___brfw > span.adProduct_num__t7R1x').text.strip())
#     print('찜 :', save)
#     print('-' * 50)
#     writer.writerow([title, price, rating, num, save])
#   except Exception as e:
#     print('에러 :', e)
# f.close()

# 실제상품 40개
pro_lists = data.select('div.product_item__MDtDF')
# csv 저장
f = open('c1025/naver/nshop.csv', 'a', encoding='UTF-8-sig', newline='')
writer = csv.writer(f)
for i, pro_list in enumerate(pro_lists):
  try:
    print(f'{i + 1}.')
    title = pro_list.select_one('div.product_title__Mmw2K > a').text.strip()
    print('상품명 :', title)
    price = int(pro_list.select_one('span.price_num__S2p_v > em').text.strip().replace(',', ''))
    print('가격 :', price)
    rating = float(pro_list.select_one('span.product_grade__IzyU3').text.replace('\n','').replace(' ','').strip()[2:])
    print('평점 :', rating)

    # 1.7만, 700, 1300
    num = pro_list.select_one('div.product_etc_box__ElfVA > a > em').text.strip().replace('\n', '').replace(' ', '').replace(',', '')[1:-1]
    # 형태에 따라 변환
    if '만' in num: num = float(num[:-1]) * 10000
    else: num = float(num)
    print('평가수 :', num)
    save = int(pro_list.select_one('div.product_etc_box__ElfVA > span.product_etc__LGVaW > span.product_num__fafe5').text.strip().replace(',', ''))
    print('찜 :', save)
    print('-' * 50)
    writer.writerow([title, price, rating, num, save])
  except Exception as e:
    print("에러 :", e)
f.close()