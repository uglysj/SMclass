import oracledb

# DB연결 함수선언
def connects():
  user = 'ora_user'
  password = '1111'
  dsn = 'localhost:1521/xe'
  try: conn = oracledb.connect(user = user, password = password, dsn = dsn)
  except Exception as e: print('예외 발생 :', e)
  return conn

while True:
  print('[ 학생성적프로그램 ]')
  print('1. 학생성적입력')
  print('2. 학생성적출력')
  print('3. 학생성적검색')
  print('0. 프로그램종료')
  choice = input('원하는 번호를 입력하세요.>> ')

  if choice == '1':
    conn = connects()
    print('[ 학생성적 입력 ]')
    cursor = conn.cursor()
    sql = 'select students_seq.currval from dual'
    cursor.execute(sql)
    row = cursor.fetchone()
    cursor.close()
    no = row[0]
    name = input(f'{no}번째. 학생이름을 입력하세요.>> ')
    kor = int(input('국어 점수를 입력하세요.>> '))
    eng = int(input('영어 점수를 입력하세요.>> '))
    math = int(input('수학 점수를 입력하세요.>> '))
  elif choice == '2':
    pass
  elif choice == '3':
    pass
  elif choice == '0':
    print('프로그램을 종료합니다.')
    break


# 학생성적프로그램
# 1. 학생성적입력
# 2. 학생성적출력
# 3. 학생성적검색
# students 테이블 사용해서
# 시퀀스 students_seq 생성
# 번호, 김유신, 99, 98, 96 합계, 평균, 등수, 입력일