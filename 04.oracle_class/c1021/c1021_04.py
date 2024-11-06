import requests
from bs4 import BeautifulSoup

url = 'https://news.naver.com/main/ranking/popularDay.naver'
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36'}
res = requests.get(url, headers=headers)
res.raise_for_status()

# with open('c1021/1.html', 'w', encoding='UTF-8') as f:
#   f.write(res.text)

# html, css 정보를 가진 소스변경
soup = BeautifulSoup(res.text, 'lxml') # str -> html, css 태그가 사용할 수 있도록 저장

# BeautifulSoup 사용
# 태그 출력, 태그 글자 출력
print(soup.title) # title 태그
print(soup.title.text) # title 태그안에 문자열 출력 - text, get_text()
print("없는 태그 :", soup.titletitle) # 없는 태그 입력시 None
# print("없는 태그 :", soup.titletitle.text) # 없을 시 에러 발생
print(soup.a) # 첫번째 a 태그를 가져옴.
print(soup.a.next.next) # next 다음 태그를 가져옴.
# 태그 속성 출력
print(soup.a.attrs) # 태그의 속성 값을 가져옴 : 딕셔너리 형태
print(soup.a['href']) # a태그의 href 속성 값을 가져옴.

# 특정정보를 출력
# print(soup.find('div', attrs={'id': 'header'}))
print(soup.find('div', {'id': 'header'})) # div 태그 중 id='header'
print(soup.find('h2', {'class': 'rankingnews_tit'}).text) # h2 태그 중 class='rankingnews_tit'의 내용 출력
print(soup.find_all('div')) # 모든 div 태그를 출력
print(len(soup.find_all('div'))) # 모든 div 태그 개수 출력
print(type(soup.find_all('div')))

# soup.prettify() 정보 저장
# with open('c1021/2.html', 'w', encoding='UTF-8') as f:
#   # soup.prettify() 는 html을 보기 좋게 만들어줌.
#   f.write(soup.prettify())

print("완료")