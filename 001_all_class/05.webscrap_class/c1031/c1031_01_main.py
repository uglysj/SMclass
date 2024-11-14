import func

while True:
  # 시작화면 출력
  choice = func.screen()  

  if choice == '1':
    # 로그인 부분
    func.memLogin()
  elif choice == '2':
    # 비밀번호 찾기 부분
    func.findPw()
  elif choice == '3':
    # 회원가입 부분
    pass
  elif choice == '4':
    print("프로그램을 종료합니다.")
    break