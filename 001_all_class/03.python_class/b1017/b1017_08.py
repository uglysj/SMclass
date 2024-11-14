import datetime, os
session_info = {}

#### member.csv 파일 불러오기 ####
members = []
m_title = ['id', 'pw', 'name', 'nicName', 'address', 'money']
f = open('b1017/member.csv', 'r', encoding='UTF-8')
while True:
  line = f.readline().rstrip()
  if not line: break
  s = line.split(',')
  s[5] = int(s[5])
  members.append(dict(zip(m_title, s)))
f.close()
# ---------------------------- #
#### cart.txt 파일 불러오기 ####
cartNo = 0
cart = []
c_keys = ['cNo', 'id', 'name', 'pCode', 'pName', 'price', 'date']
c_title = ['번호', '아이디', '이름', '상품코드', '상품명', '가격', '구매일자']
if os.path.exists("b1017/cart.txt"):
  cF = open('b1017/cart.txt', 'r', encoding='UTF-8')
  while True:
    cline = cF.readline().strip()
    if not cline: break
    s = cline.split(',')
    s[0] = int(s[0]); s[5] = int(s[5])
    cart.append(dict(zip(c_keys, s)))
  cF.close()
# ---------------------------- #
#### product.txt 파일 불러오기 ####
product = []
p_keys = ['pNo', 'pCode', 'pName', 'price', 'color']
if os.path.exists('b1017/product.txt'):
  pF = open('b1017/product.txt', 'r', encoding='UTF-8')
  while True:
    pline = pF.readline().rstrip()
    if not pline: break
    p = pline.split(',')
    p[0] = int(p[0]); p[3] = int(p[3])
    product.append(dict(zip(p_keys, p)))
  pF.close()
# ---------------------------- #

########## 함수 선언 ##########
def buy(cartNo, product, session_info, choice):
  print(f"{product[choice - 1]['pName']}가 구매되었습니다.\n")
  now = datetime.datetime.now()
  today = now.strftime("%Y-%m-%d %H:%M:%S")
  c = {'cNo': cartNo + 1, 'id': session_info['id'], 'name': session_info['name'], 'pCode': product[choice - 1]['pCode'], 'pName': product[choice - 1]['pName'], 'price': product[choice - 1]['price'], 'date': today}
  cart.append(c)
  cartNo += 1
  session_info['money'] -= product[choice - 1]['price']
  
  return cartNo
# -------------------------- #
def buy_money(session_info):
  print(f"현재 잔액 : {session_info['money']:,}원")
  session_info['money'] += int(input("충전할 금액을 입력하세요. >> "))
  print(f"충전 후 잔액 : {session_info['money']:,}원\n")
# -------------------------- #


########## 프로그램 시작 ##########
while True:
  print("[ 메인 화면 ]"); print("-" * 30)
  print("1. 로그인")
  print("2. 회원가입")
  print("0. 종료"); print("-" * 30)
  choice = input("원하는 번호를 입력하세요.>> ")
  
  chk = 0
  if choice == '1':
    while True:
      input_id = input("아이디를 입력하세요.>> ")
      input_pw = input("패스워드를 입력하세요.>> ")
      for m in members:
        if input_id == m['id'] and input_pw == m['pw']:
          session_info = m
          print("로그인 되었습니다.\n"); chk = 1
          break
        else:
          print("아이디 또는 패스워드가 틀렸습니다. 다시 입력해주세요.\n")
          break
      if chk == 0: continue
      else:
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
            cartNo = buy(cartNo, product, session_info, choice)
          elif choice == 2:
            cartNo = buy(cartNo, product, session_info, choice)
          elif choice == 3:
            cartNo = buy(cartNo, product, session_info, choice)
          elif choice == 4:
            cartNo = buy(cartNo, product, session_info, choice)
          elif choice == 8:
            pass
          elif choice == 9:
            buy_money(session_info)
  elif choice == '2':
    pass
  elif choice == '0':
    print("프로그램을 종료합니다.")
    break