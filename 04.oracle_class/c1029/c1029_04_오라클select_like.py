import oracledb

# DB연결 함수선언
def connections():
  try:
    conn = oracledb.connect(user='ora_user', password='1111', dsn='localhost:1521/xe')
  except Exception as e: print('예외 발생 :', e)
  return conn

# 함수호출
conn = connections()
cursor = conn.cursor()

# 월급 4000 ~ 8000 사이의 사원을 모두 출력하시오.
# 범위를 입력받아서 그 사이의 사원을 출력하시오.
num1 = input('첫번째 숫자 입력 >> ')
num2 = input('두번째 숫자 입력 >> ')
sql = 'select employee_id, emp_name, salary from employees where salary BETWEEN :num1 and :num2 order by salary'
cursor.execute(sql, num1=num1, num2=num2)

# employees 테이블에서 이름이 a가 포함되어 있는 모든 컬럼 출력
# search = input('검색할 이름을 입력하세요. >> ')
# search = f'%{search}%'
# sql = "select * from employees where emp_name like :search"
# cursor.execute(sql, search=search)

# search = input('번호검색 >> ')
# 키워드
# sql = "select * from employees where employee_id >= :search"
# cursor.execute(sql, search=search)
# 번호순서
# sql = "select * from employees where employee_id >= :1"
# cursor.execute(sql, [search])

title = ['employee_id', 'emp_name', 'salary']
a_list = [] # dict 타입으로 변경해서 저장
rows = cursor.fetchall()
for row in rows:
  a_list.append(dict(zip(title, row)))
print(a_list)

conn.close()