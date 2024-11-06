import time, csv, smtplib
from email.mime.text import MIMEText # email 발송관련
from email.mime.multipart import MIMEMultipart # email 첨부파일관련
from email.mime.application import MIMEApplication # email 첨부파일관련
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

smtpName = 'smtp.naver.com'
smtpPort = 587

# 자신의 네이버메일주소, pw, 받는사람이메일주소
sendEmail = 'sjlee_0220@naver.com'
password = ''
recvEmail = 'anjgkwl153@naver.com'

title = '제목 : 파이썬 이메일 보내기 안내'
content = '파일을 첨부합니다.'

msg = MIMEMultipart()
msg['Subject'] = title
msg['From'] = sendEmail
msg['To'] = recvEmail
msg.attach(MIMEText(content))

# 파일첨부
with open('c1025/naver/nshop.csv', 'rb') as f:
  attachment = MIMEApplication(f.read()) # 파일첨부
  attachment.add_header('Content-Disposition', 'attachment', filename='nshop.csv')
  msg.attach(attachment)

s = smtplib.SMTP(smtpName, smtpPort)
s.starttls() # 보안검증
s.login(sendEmail, password)
s.sendmail(sendEmail, recvEmail, msg.as_string())
print('msg :')
print(msg.as_string())
s.quit()

print("메일이 발송되었습니다.")