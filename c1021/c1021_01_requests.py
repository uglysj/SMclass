# 웹 스크래핑(web scraping)
# pip install requests / pip install beautifulsoup4 / pip install lxml

# 웹 스크래핑 세팅
import requests
# res = requests.get('https://www.google.com') # html 소스를 가져옴.
res = requests.get('https://www.naver.com') # html 소스를 가져옴.
# res = requests.get('https://www.melon.com/') # html 소스를 가져옴.
res.raise_for_status() # 에러 시 종료
# print(res.text) # html 소스 출력

# requests를 사용하여 정보를 가져올 시 
# 제이쿼리, 자바스크립트, 외부페이지, react, vue... 비동기식으로 작동되는 코드는 가져오지 못함.

print('총 문자 길이 :', len(res.text))

# 웹 소스코드 파일 저장
# f = open('c1021/a.html', 'w', encoding='UTF-8')
# f.write(res.text)
# f.close()

# f.close()를 안해도 자동으로 닫힘.
with open('c1021/naver.html', 'w', encoding='UTF-8') as f:
  f.write(res.text)

# if res.status_code == 200:
#   print(res.text)
# else:
#   print("접근할 수 없습니다.")
# print("응답 코드 :", res.status_code)