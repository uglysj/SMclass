## 학생성적 출력을 하시오.
import oracledb

conn = oracledb.connect(user='ora_user', password='1111', dsn='localhost:1521/xe')

cursor = conn.cursor()

sql = 'select * from students'
cursor.execute(sql)

title = ['번호', '이름', '국어', '영어', '수학', '합계', '평균', '등수', '등록일']
for i, t in enumerate(title):
  if i == 1: print(f'{t:10s}', end='\t')
  else: print(t, end='\t')
print(); print('-' * 80)

rows = cursor.fetchall()
for row in rows:
  for i, r in enumerate(row):
    if i == 1: print('{:10s}'.format(r), end='\t')
    elif i == 6: print(f'{r:.2f}', end='\t')
    elif i == 8: print(r.strftime('%Y-%m-%d'), end='\t')
    else: print(r, end='\t')
  print()

conn.close()