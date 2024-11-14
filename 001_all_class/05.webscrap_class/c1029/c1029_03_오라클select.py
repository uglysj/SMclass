import oracledb

# sql developer 실행
conn = oracledb.connect(user='ora_user', password='1111', dsn='localhost:1521/xe')

# sql 창이 열림
cursor = conn.cursor()

# sql 작성, 실행
# no = input("숫자를 입력하세요 >> ")
num = input('숫자를 입력하세요(,해서 입력하시오.) >> ')
n_list = num.split(',')
num2 = 20

# no = 10, 20, 30을 검색해서 출력하시오.
# sql = 'select * from students where no in(:no1, :no2, :no3)'
# cursor.execute(sql, no1=no1, no2=no2, no3=no3)

# n_list = [no1, no2, no3]
# 3. excut 함수: 리스트 값 전달
# excute 뒤에는 dict, list, tuple 타입만 가능
sql = 'select * from students where no in(:1, :2)'
cursor.execute(sql, [num, num2])

# 2. excute 함수: 변수 key값 추가
# sql = 'select * from students where no >= :no'
# cursor.execute(sql, no=no)

# 1. 문자열 함수 f 사용
# sql = f'select * from students where no >= {num}'

# 데이터 가져오기 - fetchone(): 1개, fetchmany(10): 정한 숫자만큼, fetchall(): 모두
rows = cursor.fetchall()

title = ['번호', '이름', '국어', '영어', '수학', '합계', '평균', '등수', '등록일']
for i, t in enumerate(title):
  if i == 1: print(f'{t:8s}', end='\t')
  else: print(t, end='\t')
print(); print('-' * 80)

for row in rows:
  for i, r in enumerate(row):
    # strftime() 함수: 날짜포맷함수 %Y - 2024, %y - 24
    if i == 1: print(f'{r:10s}', end='\t')
    elif i == 6: print(f'{r:.2f}', end='\t')
    elif i == 8: print(r.strftime('%Y-%m-%d'), end='\t')
    else: print(r, end='\t')
  print()

# 종료
conn.close()