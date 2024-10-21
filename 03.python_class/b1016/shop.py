import datetime
member = []
m_keys = ['id', 'pw', 'name', 'nicName', 'address', 'money']
# member.txt 파일을 읽기
# member 저장
f = open('member.txt', 'r', encoding='UTF-8')
while True:
  line = f.readline()
  if not line: break
  s = line.strip().split(',')
  s[5] = int(s[5])
  member.append(dict(zip(m_keys, s)))
f.close()

product = [
  {'pNo': 1, 'pCode': 't001', 'pName': '삼성TV', 'price': 2000000, 'color': 'black'},
  {'pNo': 2, 'pCode': 'g001', 'pName': 'LG냉장고', 'price': 3000000, 'color': 'white'},
  {'pNo': 3, 'pCode': 'h001', 'pName': '하만카돈스피커', 'price': 500000, 'color': 'black'},
  {'pNo': 4, 'pCode': 'w001', 'pName': '세탁기', 'price': 1000000, 'color': 'silver'},
]
cartNo = 0
cart = []
c_keys = ['cNo', 'id', 'name', 'pCode', 'pName', 'price', 'date']
cF = open('cart.txt', 'r', encoding='UTF-8')
while True:
  line = cF.readline()
  if not line: break
  s = line.strip().split(',')
  s[0] = int(s[0]); s[5] = int(s[5])
  cart.append(dict(zip(c_keys, s)))
cF.close()

session_info = {}
p_title = ['번호', '아이디', '이름', '상품코드', '상품명', '가격', '구매일자']

##### 함수 선언 #####
def buy(choice, cartNo):
  print(f"{product[choice - 1]['pName']}를 구매하셨습니다.")
  print("구매내역에 등록합니다.\n")
  # 로그인정보 - session_info
  now = datetime.datetime.now()
  today = now.strftime('%Y-%m-%d %H:%M:%S')
  c = {'cNo': cartNo + 1, 'id': session_info['id'], 'name': session_info['name'], 'pCode': product[choice - 1]['pCode'], 'pName': product[choice - 1]['pName'], 'price': product[choice - 1]['price'], 'date': today}
  session_info['money'] -= product[choice - 1]['price']
  cart.append(c)
  cartNo += 1
  return cartNo
# ------------------------------------------ #
def buy_output():
  print(f"{p_title[0]}\t{p_title[1]}\t{p_title[2]}\t{p_title[3]}\t{p_title[4]:12s}\t{p_title[5]}\t{p_title[6]}")
  print("-" * 80)

  sum = 0
  for c in cart:
    sum += c['price']
    print(f"{c['cNo']}\t{c['id']}\t{c['name']}\t{c['pCode']}\t{c['pName']:14s}\t{c['price']}\t{c['date']}")
  print(); 

  print(f"총 구매 금액 : {sum:,}", end='\t'); print(f"총 구매 개수 : {len(cart)}")
# ------------------------------------------ #
def buy_money():
  print("[ 금액충전 ]")
  print(f"현재 잔액 : {session_info['money']:,}")
  session_info['money'] += int(input("충전 금액 입력 >> "))
  print(f"충전 후 잔액 : {session_info['money']:,}")
# ------------------------------------------ #
def buy_save():
  f = open('member.txt', 'w', encoding='UTF-8')
  for m in member:
    f.write(f'{m['id']},{m['pw']},{m['name']},{m['nicName']},{m['address']},{m['money']}\n')
  f.close() 

  cF = open('cart.txt', 'a', encoding='UTF-8')
  for c in cart:
    cF.write(f"{c['cNo']},{c['id']},{c['name']},{c['pCode']},{c['pName']},{c['price']},{c['date']}\n")
  cF.close()

  print("내용 저장이 완료되었습니다.\n")

##### 프로그램 시작 #####
while True:
  print("[ 로그인 화면 ]")
  input_id = input("아이디를 입력하세요.>> ")
  input_pw = input("패스워드를 입력하세요.>> ")

  # DB에서 가져옴. member 데이터를 가지고 비교
  chk = 0
  for m in member:
    if input_id == m['id'] and input_pw == m['pw']:
      print("SM-SHOP에 오신 것을 환영합니다."); chk = 1
      session_info = m
      break
  if chk == 0:
    print("아이디 또는 패스워드가 일치하지 않습니다.")
  else:
    break

while True:
  print("                 [ SM-SHOP ]")
  print(f"                             닉네임 : {session_info['nicName']} 님")
  print(f"                             잔액 : {session_info['money']:,} 원")
  print("1. 삼성TV - 2,000,000")
  print("2. LG냉장고 - 3,000,000")
  print("3. 하만카돈스피커 - 500,000")
  print("4. 세탁기 - 1,000,000")
  print("7. 내용저장")
  print("8. 구매내역")
  print("9. 금액충전")
  choice = int(input("구매하려는 상품번호를 입력하세요.>> "))
  
  if choice == 1:
    cartNo = buy(choice, cartNo) # 상품구매함수 호출
  elif choice == 2:
    cartNo = buy(choice, cartNo) # 상품구매함수 호출
  elif choice == 3:
    cartNo = buy(choice, cartNo) # 상품구매함수 호출
  elif choice == 4:
    cartNo = buy(choice, cartNo) # 상품구매함수 호출
  elif choice == 7:
    buy_save()
  elif choice == 8:
    buy_output()
  elif choice == 9:
    buy_money()