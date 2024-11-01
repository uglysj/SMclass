# 학생성적프로그램 students 테이블 사용
# 1. 학생성적입력
# 시퀀스 students_seq 생성
# 번호, 김유신, 99, 98, 96, 합계, 평균, 등수, 입력일
# 2. 학생성적출력
# 3. 학생성적검색

import oracledb

# 출력 타이틀
title = ['번호', '이름', '국어', '영어', '수학', '합계', '평균', '등수', '등록일']

# DB 접속 함수
def connects():
  user = 'ora_user'
  password = '1111'
  dsn = 'localhost:1521/xe'
  try: conn = oracledb.connect(user=user, password=password, dsn=dsn)
  except Exception as e: print('예외 발생 :', e)
  return conn

# 타이틀 출력 함수
def stu_title():
  for i, t in enumerate(title):
    if i == 1: print(f"{t:12s}", end='\t')
    else: print(t, end='\t')
  print(); print('-' * 85)

# 학생입력 함수
def stu_input():
  print('[ 학생성적입력 ]\n')
  
  name = input('학생 이름 입력 >> ')
  kor = int(input('국어 점수 입력 >> '))
  eng = int(input('영어 점수 입력 >> '))
  math = int(input('수학 점수 입력 >> '))

  conn = connects()
  cursor = conn.cursor()
  sql = 'insert into students values(students_seq.nextval, :name, :kor, :eng, :math, :kor + :eng + :math, (:kor + :eng + :math) / 3.0, 0, sysdate)'
  cursor.execute(sql, name=name, kor=kor, eng=eng, math=math)
  conn.commit()
  conn.close()

  print('저장되었습니다.')

# 학생출력 함수
def stu_output():
  print('[ 학생성적출력 ]\n')

  stu_title()

  conn = connects()
  cursor = conn.cursor()
  sql = 'select * from students'
  cursor.execute(sql)
  rows = cursor.fetchall()
  conn.close()

  for row in rows:
    for i, r in enumerate(row):
      if i == 1: print(f"{r:12s}", end='\t')
      elif i == 6: print(f"{r:.2f}", end='\t')
      elif i == 8: print(f'{r.strftime('%Y/%m/%d')}', end='\t')
      else: print(r, end='\t')
    print()

# 학생검색 함수
def stu_search():
  print('[ 학생성적검색 ]\n')
  
  name = input('찾으려는 학생 이름 입력 >> ')

  conn = connects()
  cursor = conn.cursor()
  sql = 'select * from students where name = :name'
  cursor.execute(sql, name=name)
  row = cursor.fetchone()
  conn.close()
  if row == None: 
    print('찾으려는 학생이 없습니다.')
    exit(0)
  
  print(f'{name} 학생을 찾았습니다.\n')
  
  stu_title()

  for i, r in enumerate(row):
    if i == 1: print(f"{r:12s}", end='\t')
    elif i == 6: print(f"{r:.2f}", end='\t')
    elif i == 8: print(f'{r.strftime('%Y/%m/%d')}', end='\t')
    else: print(r, end='\t')

### 프로그램 시작 부분 ###
print('[ 학생성적 프로그램 ]')
print('1. 학생성적입력')
print('2. 학생성적출력')
print('3. 학생성적검색')
choice = input('원하는 번호를 입력하세요.>> ')

if choice == '1':
  stu_input()
elif choice == '2':
  stu_output()
elif choice == '3':
  stu_search()