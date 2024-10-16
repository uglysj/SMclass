import datetime
mem_info = {}
product = [
  {'pNo': 1, 'pCode': 'g001', 'pName': '양문형냉장고', 'price': 1419600, 'color': 'silver'},
  {'pNo': 2, 'pCode': 's001', 'pName': '식기세척기', 'price': 1263000, 'color': 'white'},
  {'pNo': 3, 'pCode': 'b001', 'pName': '압력밥솥', 'price': 198560, 'color': 'silver'}
]
cartNo = 0
cart_title = ['번호', '아이디', '이름', '상품코드', '상품명', '상품가격', '구매날짜']

# 회원정보 불러오기
member = []
mem_title = ['id', 'pw', 'name', 'nicName', 'address', 'money']
f = open('member.txt', 'r', encoding='UTF-8')
while True:
  line = f.readline()
  if not line: break
  m = line.strip().split(',')
  m[5] = int(m[5])
  member.append(dict(zip(mem_title, m)))

# 카트정보 불러오기
cart = []
c_title = ['cNo', 'id', 'name', 'pCode', 'pName', 'price', 'date']
cF = open('cart.txt', 'r', encoding='UTF-8')
while True:
  cline = cF.readline()
  if not cline: break
  c = cline.strip().split(',')
  c[0] = int(c[0]); c[5] = int(c[5])
  cart.append(dict(zip(c_title, c)))

##### 함수 선언 #####
def buy(cartNo, choice):
  print(f"{product[choice - 1]['pName']} 상품이 결제되었습니다.")
  print("주문내역에 저장합니다.\n")
  now = datetime.datetime.now()
  today = now.strftime("%Y-%m-%d %H:%M:%S")
  c = {'cNo': cartNo + 1, 'id': mem_info['id'], 'name': mem_info['name'], 'pCode': product[choice - 1]['pCode'], 'pName': product[choice - 1]['pName'], 'price': product[choice - 1]['price'], 'date': today}
  cart.append(c)
  mem_info['money'] -= product[choice - 1]['price']
  cartNo += 1
  
  return cartNo
# ---------------------------------- #
def buy_cash():
  print(f"현재 보유 잔액 : {mem_info['money']:,}원")
  mem_info['money'] += int(input("충전할 금액을 입력하세요.>> "))
  print(f"충전 후 보유 잔액 : {mem_info['money']:,}원\n")
# ---------------------------------- #
####################

# 로그인 하기
print("[ SM SHOP ]")
while True:
  print("[ 로그인 ]")
  input_id = input("아이디를 입력하세요.>> ")
  input_pw = input("패스워드를 입력하세요.>> ")

  chk = 0
  for m in member:
    if input_id == m['id'] and input_pw == m['pw']:
      chk = 1; mem_info = m
      print("로그인 되었습니다.\n"); break    
  if chk == 0:
    print("아이디 또는 패스워드가 틀립니다. 다시 입력해주세요.\n")
  else:
    break

# 상품구매창
while True:
  print(f"{mem_info['nicName']}님\n잔액 : {mem_info['money']:,}원\n")
  print("[ 주방가전 상품목록 ]"); print("-" * 20)
  print("1. 양문형냉장고")
  print("삼성전자 비스포크 4도어")
  print("1,419,600원"); print("-" * 20)
  print("2. 식기세척기")
  print("LG전자 디오스")
  print("1,263,000원"); print("-" * 20)
  print("3. 압력밥솥")
  print("쿠첸 초고압 압력밥솥")
  print("198,560원"); print("-" * 20)
  print("9. 금액충전\t99. 구매내역")
  choice = int(input("원하는 번호를 선택하세요.>> "))

  if choice == 1:
    cartNo = buy(cartNo, choice)
  elif choice == 2:
    cartNo = buy(cartNo, choice)
  elif choice == 3:
    cartNo = buy(cartNo, choice)
  elif choice == 9:
    buy_cash()
  elif choice == 99:
    print(f"{cart_title[0]}\t{cart_title[1]}\t{cart_title[2]}\t{cart_title[3]}\t{cart_title[4]:10s}\t{cart_title[5]}\t{cart_title[6]}")
    print("-" * 80)

    for c in cart:
      print(f"{c['cNo']}\t{c['id']}\t{c['name']}\t{c['pCode']}\t{c['pName']:14s}\t{c['price']}\t{c['date']}")
    print()