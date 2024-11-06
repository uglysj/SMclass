import oracledb
s_title = ['번호', '이름', '국어', '영어', '수학', '합계', '평균', '등수', '등록일']

# 학생타이틀 출력 함수선언
def stuTitle():
  for i, s in enumerate(s_title):
    if i == 1: print('{:12s}'.format(s), end='\t')
    else: print(s, end='\t')
  print(); print('-' * 80)

# 메인화면 출력 함수선언
def main_print():
  print('[ 학생성적프로그램 ]')
  print('1. 학생성적입력')
  print('2. 학생성적출력')
  print('3. 학생성적검색')
  print('4. 학생성적정렬') # 이름순차정렬, 이름역순정렬, 합계순차정렬, 합계역순정렬
  print('5. 등수처리')
  print('0. 프로그램종료')
  choice = input('원하는 번호를 입력하세요.>> ')
  return choice

# DB연결 함수선언
def connects():
  user = 'ora_user'
  password = '1111'
  dsn = 'localhost:1521/xe'
  try: conn = oracledb.connect(user = user, password = password, dsn = dsn)
  except Exception as e: print('예외 발생 :', e)
  return conn

# 1. 학생성적입력 함수선언
def stuInput():
  conn = connects()
  print('[ 학생성적 입력 ]')
  cursor = conn.cursor()
  name = input('학생이름을 입력하세요.>> ')
  kor = int(input('국어 점수를 입력하세요.>> '))
  eng = int(input('영어 점수를 입력하세요.>> '))
  math = int(input('수학 점수를 입력하세요.>> '))
  total = kor + eng + math
  avg = total / 3

  # list
  s_list = [name, kor, eng, math, total, avg]
  # insert, update, delete를 할 경우 conn.commit() 해야 함.
  sql = 'insert into students values(students_seq.nextval, :1, :2, :3, :4, :5, :6, 0, sysdate)'
  cursor.execute(sql, s_list)
  conn.commit()
  conn.close()
  print('학생성적이 저장되었습니다.\n')

# 2-1. 출력함수 선언
def stuPrint(*data):
  print('[ 학생성적 출력 ]')
  stuTitle()

  # DB연결
  conn = connects()
  cursor = conn.cursor()

  if len(data) == 1:
    cursor.execute(data[0])
  else:
    cursor.execute(data[0], search = data[1])  
  
  rows = cursor.fetchall()
  if rows == None: 
    print('데이터가 없습니다.')
    return
  else:
    for row in rows:
      for i, r in enumerate(row):
        if i == 1: print('{:12s}'.format(r), end='\t')
        else: print(r, end='\t')
      print()
  print('데이터 출력 완료!')
  conn.close()

# 2. 학생성적출력 함수선언
def stuOutput():
  sql = "select no, name, kor, eng, math, total, round(avg, 2), rank, to_char(sdate, 'yyyy-mm-dd') from students"
  stuPrint(sql)

# 3. 학생성적검색 함수선언
def stuSearch():
  print('[ 학생성적 검색 ]')
  print('1. 이름으로 검색')
  choice = input('원하는 번호를 입력하세요.>> ')

  if choice == '1':
    print('[ 이름으로 검색 ]')
    search = input('찾고자 하는 이름을 입력하세요.>> ')
    search = f'%{search}%'
    sql = "select no, name, kor, eng, math, total, round(avg, 2), rank, to_char(sdate, 'yyyy-mm-dd') from students where name like :search"
    
    stuPrint(sql, search)

# 4. 학생성적정렬 함수선언
def stuSort():
  print('[ 학생성적 정렬 ]')
  print('1. 이름 순차 정렬')
  print('2. 이름 역순 정렬')
  print('3. 합계 순차 정렬')
  print('4. 합계 역순 정렬')
  choice = input('원하는 번호를 입력하세요.>> ')

  if choice == '1':
    sql = "select no, name, kor, eng, math, total, round(avg, 2), rank, to_char(sdate, 'yyyy-mm-dd') from students order by name"
  elif choice == '2':
    sql = "select no, name, kor, eng, math, total, round(avg, 2), rank, to_char(sdate, 'yyyy-mm-dd') from students order by name desc"
  elif choice == '3':
    sql = "select no, name, kor, eng, math, total, round(avg, 2), rank, to_char(sdate, 'yyyy-mm-dd') from students order by total"
  elif choice == '4':
    sql = "select no, name, kor, eng, math, total, round(avg, 2), rank, to_char(sdate, 'yyyy-mm-dd') from students order by total desc"
  
  stuPrint(sql)

# 5. 등수처리 함수선언
def stuRank():
  print('[ 등수 처리 ]')
  conn = connects()
  cursor = conn.cursor()
  sql = 'update students a set rank = (select ranks from (select no, rank() over(order by avg desc) ranks from students) b where a.no = b.no)'
  cursor.execute(sql)
  conn.commit()
  conn.close()
  
  print('등수처리가 완료되었습니다.')