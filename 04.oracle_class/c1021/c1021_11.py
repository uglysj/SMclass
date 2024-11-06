import requests
from bs4 import BeautifulSoup

url = 'https://www.melon.com/index.htm'
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36'}
res = requests.get(url, headers=headers)
res.raise_for_status()
soup = BeautifulSoup(res.text, 'lxml')

hot_issue = soup.find('div', {'class': 'hot_issue'})
# title = hot_issue.find('span', {'class': 'title'}).text
# print("제목 :", hot_issue.find('span', {'class': 'title'}).text)
# print(hot_issue.find('img')['src'])
# with open(f'c1021/{title}.jpg', 'wb') as f:
#   get_img = requests.get(hot_issue.find('img')['src'])
#   f.write(get_img.content)

issue_lists = hot_issue.find_all('dl')
for idx, t in enumerate(issue_lists):
  print(t.find('span', {'class': 'title'}).text)