import time
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options

# selenium 화면을 숨김처리
options = Options()
options.add_argument('--headless')
options.add_argument('--window-size=1920,1080')
options.add_argument('User-Agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36')

url = 'https://www.whatismybrowser.com/detect/what-is-my-user-agent/'
browser = webdriver.Chrome(options=options)
browser.maximize_window()
browser.get(url)

soup = BeautifulSoup(browser.page_source, 'lxml')
data = soup.select_one('#detected_value').text
print(data)

browser.get_screenshot_as_file('c1024/user-agent.png')
input('엔터키 입력완료 >> ')