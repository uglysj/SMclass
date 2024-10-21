# members 리스트 딕셔너리 저장
members = []
m_title = ['id', 'pw', 'name', 'nicName', 'address', 'money']

# member 파일 불러오기
f = open('b1017/member.csv', 'r', encoding='UTF-8')
while True:
  line = f.readline().rstrip()
  if not line: break
  s = line.split(',')
  for i in range(len(s)):
    if s[i].isdigit(): s[i] = int(s[i])
  members.append(dict(zip(m_title, s)))
f.close()

while True:
  print("1. 회원등록")
  print("2. 회원검색")
  choice = input("원하는 번호를 입력하세요.>> ")
  if choice == '1':
    id = input("아이디를 입력하세요.>> ")
    chk = 0
    for m in members:
      if m['id'] == id:
        print(f"{id} 라는 동일한 아이디가 존재합니다. 다시 입력해주세요."); chk = 1
        break
    if chk == 1: continue
    else:
      print(f"{id} 는(은) 사용가능합니다.")
      pw = input('패스워드를 입력하세요.>> ')
      name = input("이름을 입력하세요.>> ")
      nicName = input('닉네임을 입력하세요.>> ')
      address = input('주소를 입력하세요. (시 까지만)>> ')
      money = int(input("충전 금액을 입력하세요.>> "))
      m_list = [id, pw, name, nicName, address, money]
      members.append(dict(zip(m_title, m_list)))
      print(f"{name} 님 회원가입이 완료되었습니다.")
      print(m_list); print("-" * 50); print(members)
  elif choice == '2':
    # 회원 검색
    chk = 0
    mm = []
    search_id = input("검색할 아이디를 입력하세요.>> ")
    for m in members:
      if m['id'].find(search_id) != -1:
        mm.append(m); chk = 1

    if chk == 0:
      print("검색한 아이디가 없습니다.")
    else:
      print("총 검색된 인원 :", len(mm))
      print(mm)