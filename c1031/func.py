import smtplib, random, oracledb
from email.mime.text import MIMEText

# DB연결 함수선언
def connects():
  user = 'ora_user'
  password = '1111'
  dsn = 'localhost:1521/xe'
  try: conn = oracledb.connect(user=user, password=password, dsn=dsn)
  except Exception as e: print('예외 처리 :', e)
  return conn

# 시작화면 함수선언
def screen():
  # 로그인이 되어 있지 않은 상태
  print('[ 커뮤니티 ]')
  print('1. 로그인')
  print('2. 비밀번호 찾기')
  print('3. 회원가입')
  print('4. 프로그램 종료')
  choice = input('원하는 번호를 입력하세요.>> ')
  return choice

# 1. 로그인 함수선언
def memLogin():
  user_id = input('아이디를 입력하세요.>> ')
  user_pw = input('패스워드를 입력하세요.>> ')

  # DB접속
  conn = connects()
  cursor = conn.cursor()
  sql = 'select * from member where id = :id and pw = :pw'
  cursor.execute(sql, id=user_id, pw=user_pw)
  row = cursor.fetchone()
  cursor.close()

  if row == None: print('아이디 또는 패스워드가 일치하지 않습니다. 다시 입력해주세요.'); return
  else:
    # 이후 프로그램 구성
    print(f'{row[2]} 님 환영합니다.\n')

# 임시비밀번호 생성 함수선언
def randomPw():
  a = random.randrange(0, 10000)
  ran_num = f'{a:04}'
  print('랜덤번호 :', ran_num)
  return ran_num

# 메일 발송 함수선언
def emailSend(email):
  # email 발송
  smtpName = 'smtp.naver.com'
  smtpPort = 587

  sendEmail = 'sjlee_0220@naver.com'
  password = 'ZWZJ1XWCKD2R'
  recvEmail = email

  tempPw = randomPw()
  title = '임시패스워드 안내'
  content = f'임시패스워드는 {tempPw} 입니다.'
  print('임시패스워드 :', content)

  # 설정
  msg = MIMEText(content)
  msg['Subject'] = title
  msg['From'] = sendEmail
  msg['To'] = recvEmail

  # 서버이름, 서버포트
  s = smtplib.SMTP(smtpName, smtpPort)
  s.starttls()
  s.login(sendEmail, password)
  s.sendmail(sendEmail, recvEmail, msg.as_string())

  # 메일 발송 종료
  print('메일이 발송되었습니다.\n')
  return tempPw

# 2. 비밀번호 찾기 함수선언
def findPw():
  user_id = input('아이디를 입력하세요.>> ')

  conn = connects()
  cursor = conn.cursor()
  sql = 'select * from member where id = :id'
  cursor.execute(sql, id=user_id)
  row = cursor.fetchone()

  if row == None: print("아이디가 존재하지 않습니다.\n"); return
  else:
    input(f'{row[0]} 아이디가 존재합니다. 메일을 보내려면 Enter를 입력하세요.')
    random_pw = emailSend(row[3])
    
    # 임시비밀번호를 update
    sql = 'update member set pw = :pw where id = :id'
    cursor.execute(sql, pw=random_pw, id=user_id)
    conn.commit()