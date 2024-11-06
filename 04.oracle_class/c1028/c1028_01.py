import oracledb

# oracle 연결 - sql developer 연결
conn = oracledb.connect(user='ora_user', password='1111', dsn='localhost:1521/xe')
# 연결확인
# print(conn.version)

# sql 실행창 오픈
# 검색된 1개 데이터 호출
# cursor = conn.cursor()
# sql = 'select count(*) from member'
# cursor.execute(sql)
# count1 = cursor.fetchone()
# print('개수 :', count1)

# 여러개 데이터 호출
cursor = conn.cursor()
sql = 'select * from member'
cursor.execute(sql)
rows = cursor.fetchall()

title = ['ID', 'PW', 'NAME', 'EMAIL', 'PHONE', 'GENDER', 'HOBBY', 'MDATE']
print(*title, sep='\t'); print('-' * 100)

for row in rows:
  for r in row:
    print(r, end='\t')
  print()

# print(rows[0][0], rows[0][1], rows[0][2], rows[0][3])

conn.close()