import smtplib, requests
from email.mime.text import MIMEText # email 발송관련
from email.mime.multipart import MIMEMultipart # email 첨부파일관련
from email.mime.application import MIMEApplication # email 첨부파일관련
from bs4 import BeautifulSoup

url = 'https://news.naver.com/main/ranking/popularDay.naver'
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36", 'Accept-Language' : 'ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7'}
res = requests.get(url, headers=headers)

soup = BeautifulSoup(res.text, 'lxml')
data = soup.select_one('#wrap > div.rankingnews._popularWelBase._persist > div.rankingnews_box_wrap._popularRanking > div')
boxs = data.select('div.rankingnews_box')

with open('c1025/news.txt', 'w+', encoding='UTF-8') as f:
  for box in boxs:
    name = box.select_one('strong.rankingnews_name').text
    print('언론사 :', name)
    f.write(f'언론사 : {name}\n')
    news_list = box.select('ul.rankingnews_list > li')
    for news in news_list:
      num = news.select_one('em.list_ranking_num').text
      title = news.select_one('a.list_title').text
      print(num + ".", title)
      f.write(f'{num}. {title}\n')
    print('-' * 50)

# smtpName = 'smtp.naver.com'
# smtpPort = 587

# sendmail = 'sjlee_0220@naver.com'
# password = ''
# recvmail = 'anjgkwl153@naver.com'

# title = '파이썬으로 네이버 뉴스 보내기'
# content = 'smtp를 사용하여 파일을 첨부해 보내기'

# msg = MIMEMultipart()
# msg['Subject'] = title
# msg['From'] = sendmail
# msg['To'] = recvmail
# msg.attach(MIMEText(content))

# with open('c1025/news1.txt', 'rb') as f:
#   attachment = MIMEApplication(f.read())
#   attachment.add_header('Content-Disposition', 'attachment', filename='news1.txt')
#   msg.attach(attachment)

# s = smtplib.SMTP(smtpName, smtpPort)
# s.starttls()
# s.login(sendmail, password)
# s.sendmail(sendmail, recvmail, msg.as_string())
# s.quit()

# print("메일 발송이 완료되었습니다.")