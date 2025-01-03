# 입력한 달 이상의 입사한 사원을 출력하시오.
import oracledb

def connects():
  user = 'ora_user'
  password = '1111'
  dsn = 'localhost:1521/xe'
  try: conn = oracledb.connect(user=user, password=password, dsn=dsn)
  except Exception as e: print("예외 발생 :", e)
  return conn

d_day = int(input('숫자를 입력하세요.>> '))
print(d_day)

conn = connects()
cursor = conn.cursor()
# sql = 'select emp_name, hire_date from employees where substr(hire_date, 4, 2) > :month'
# cursor.execute(sql, month=d_day)
sql = 'select hire_date, substr(hire_date, 4, 2) hire_date2 from employees where substr(hire_date, 4, 2) > :d'
cursor.execute(sql, d=d_day)
rows = cursor.fetchall()

for row in rows:
  # print(row[0], row[1].strftime('%Y/%m/%d'))
  print(row)

conn.close()