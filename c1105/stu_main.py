import stu_func

while True:
  choice = stu_func.main_print() # 메인화면 출력부분

  if choice == '1':
    stu_func.stuInput()
  elif choice == '2':
    stu_func.stuOutput()
  elif choice == '3':
    stu_func.stuSearch()
  elif choice == '4':
    stu_func.stuArray()
  elif choice == '5':
    stu_func.stuRank()
  elif choice == '0':
    print('프로그램을 종료합니다.')
    break