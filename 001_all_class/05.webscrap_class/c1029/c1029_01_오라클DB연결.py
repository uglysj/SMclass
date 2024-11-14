import oracledb

# sql developer 실행
conn = oracledb.connect(user='ora_user', password='1111', dsn='localhost:1521/xe')

# sql 창이 열림
cursor = conn.cursor()

# sql 작성, 실행
sql = 'select * from students'
cursor.execute(sql)

# 데이터 가져오기 - fetchone(): 1개, fetchmany(10): 정한 숫자만큼, fetchall(): 모두
rows = cursor.fetchall()

title = ['번호', '이름', '국어', '영어', '수학', '합계', '평균', '등수', '등록일']
for i, t in enumerate(title):
  if i == 1: print(f'{t:10s}', end='\t')
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