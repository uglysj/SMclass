import time, csv
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# 제목, 금액, 평점, 평가수, 찜 정보를 1-5 페이지까지 가져와서
# 평점 4.8이상, 평가수 1000명 이상 인 상품을 csv파일로 저장하고, 출력하시오
# browser = webdriver.Chrome()
# browser.maximize_window()
# for i in range(5):
#   url = f'https://search.shopping.naver.com/search/all?adQuery=%EB%AC%B4%EC%84%A0%EB%A7%88%EC%9A%B0%EC%8A%A4&origQuery=%EB%AC%B4%EC%84%A0%EB%A7%88%EC%9A%B0%EC%8A%A4&pagingIndex={i+1}&pagingSize=40&productSet=total&query=%EB%AC%B4%EC%84%A0%EB%A7%88%EC%9A%B0%EC%8A%A4&sort=rel&timestamp=&viewType=list'
#   browser.get(url)
#   time.sleep(2)

#   prev_height = browser.execute_script('return document.body.scrollHeight')
#   while True:
#     browser.execute_script('window.scrollTo(0, document.body.scrollHeight)')
#     time.sleep(2)
#     curr_height = browser.execute_script('return document.body.scrollHeight')
#     if prev_height == curr_height: break
#     prev_height = curr_height

#   soup = BeautifulSoup(browser.page_source, 'lxml')
#   with open(f'c1025/naver/shopping{i+1}.html', 'w+', encoding='UTF-8') as f:
#     f.write(soup.prettify())
#   time.sleep(5)

def num_chg(p_num):
    f_num = p_num[:-1].replace('.', '')
    if len(f_num) < 2:
      return int(f_num) * 10000
    else:
      ff_num = int(f_num[0]) * 10000
      l_num = int(f_num[1]) * 1000
      return ff_num + l_num

p = open('c1025/naver/products.csv', 'w+', encoding='UTF-8-sig', newline='')
writer = csv.writer(p)
p.write('번호,제품명,가격,평점,평가수,찜\n')
prod = []; no = 1; cnt, fcnt, ecnt = 0, 0, 0
for i in range(5):
  with open(f'c1025/naver/shopping{i+1}.html', 'r+', encoding='UTF-8') as f:
    soup = BeautifulSoup(f, 'lxml')

  basicList = soup.select_one('#content > div.style_content__xWg5l > div.basicList_list_basis__uNBZx')
  products = basicList.select('div.product_item__MDtDF')
  for idx, product in enumerate(products):
    try:
      p_name = product.select_one('div.product_title__Mmw2K > a').text.strip()
      price = int(product.select_one('span.price_num__S2p_v > em').text.strip().replace(',', ''))
      rating = float(product.select_one('span.product_grade__IzyU3').text.replace('\n','').replace(' ','').strip()[2:])
      p_num = product.select_one('a.product_etc__LGVaW > em').text.replace('\n', '').replace(' ', '')[1:-1]
      if '만' in p_num: p_num = num_chg(p_num)
      else: p_num = int(p_num.replace(',', ''))
      p_save = int(product.select_one('span.product_num__fafe5').text.strip().replace(',', ''))

      if rating >= 4.8 and p_num >= 1000:
        print(f'{(i * 40) + idx + 1}.')
        print('제품명 :', p_name)
        print(f'가격 : {price:,}')
        print('평점 :', rating)
        print(f'평가수 : {p_num:,}')
        print(f"찜 : {p_save:,}")
        print('-' * 50)
        writer.writerow([no, p_name, price, rating, p_num, p_save])
        no += 1; cnt += 1
      else:
        print(f'{(i * 40) + idx + 1}. 조건미달'); print('-' * 50); fcnt += 1
    except Exception as e:
      print('에러 :', e); print('-' * 50); ecnt += 1

p.close()
print(f'정상 : {cnt}, 미달 : {fcnt}, 에러 : {ecnt}')