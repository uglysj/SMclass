import time
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options

# selenium 화면을 숨김처리
# options = Options()
# options.add_argument('--headless')
# options.add_argument('--window-size=1920,1080')
# options.add_argument('User-Agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36')

# for i in range(3):
#   url = f'https://www.gmarket.co.kr/n/search?keyword=%EB%85%B8%ED%8A%B8%EB%B6%81&k=53&p={i + 1}'
#   browser = webdriver.Chrome(options=options)
#   browser.maximize_window()
#   browser.get(url)
#   time.sleep(10)
#   soup = BeautifulSoup(browser.page_source, 'lxml')
#   with open(f'c1024/gmarket{i + 1}.html', 'w+', encoding='UTF-8') as f:
#     f.write(soup.prettify())
#   browser.get_screenshot_as_file(f'c1024/gmarket{i + 1}.png')

# 노트북 검색 된 사이트 1, 2, 3페이지 에서 만족도 95 이상이면서, 금액 150만원 이하, 평가수 100이상 검색하시오.
for i in range(3):
  with open(f'c1024/gmarket{i+1}.html', 'r+', encoding='UTF-8') as f:
    soup = BeautifulSoup(f, 'lxml')

  data = soup.select_one('#section__inner-content-body-container')
  lists = data.select('div.section__module-wrap > div.box__component')
  for idx, list in enumerate(lists):
    try:
      print(idx+1, list.select_one('span.text__item').text.strip())
    except Exception as e:
      print(idx+1, '에러', e)