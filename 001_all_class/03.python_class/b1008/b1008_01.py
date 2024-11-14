students = []
title = ['번호', '이름', '국어', '영어', '수학', '합계', '평균', '등수']
no, kor, eng, math, total, avg, rank = 0, 0, 0, 0, 0, 0, 0
name = ""
choice = ""
chk = 0

while True:
  print("[ 학생성적 프로그램 ]")
  print("-" * 60)
  print("0. 프로그램종료")
  print("1. 학생성적입력")
  print("2. 학생성적출력")
  print("3. 학생성적수정")
  print("4. 학생성적검색")
  print("5. 학생성적삭제")
  print("6. 학생등수처리")
  print("-" * 60)
  choice = input("원하는 번호를 입력하세요.>> ")

  if choice == '0':
    print("[ 프로그램종료 ]")
    print("프로그램을 종료합니다.")
    break
  elif choice == '1':
    print("[ 학생성적입력 ]\n")

    while True:
      no = len(students) + 1
      name = input(f"{no}번째 학생 이름 입력(0: 메뉴화면) >> ")
      if name == '0':
        print("메뉴 화면으로 돌아갑니다.\n")
        break
      kor = int(input("국어 점수 입력 >> "))
      eng = int(input("영어 점수 입력 >> "))
      math = int(input("수학 점수 입력 >> "))
      total = kor + eng + math
      avg = total / 3
      rank = 0
      
      students.append([no, name, kor, eng, math, total, avg, rank])
      print(f"{name} 학생의 성적이 저장되었습니다.\n")

  elif choice == '2':
    print("[ 학생성적출력 ]\n")

    for t in title:
      print("{}".format(t), end="\t")
    print(); print("-" * 60)

    for stu in students:
      print(f"{stu[0]}\t{stu[1]}\t{stu[2]}\t{stu[3]}\t{stu[4]}\t{stu[5]}\t{stu[6]:.2f}\t{stu[7]}")
    print()
  
  elif choice == '3':
    print("[ 학생성적수정 ]\n"); chk = 0
    
    name = input("검색하려는 학생 이름 입력 >> ")
    for stu in students:
      if name == stu[1]:
        print(f"{name} 학생을 찾았습니다.\n"); chk = 1

        print("수정하려는 과목 선택")
        print("0. 메뉴화면")
        print("1. 국어점수")
        print("2. 영어점수")
        print("3. 수학점수")
        choice = input("원하는 번호 입력 >> ")

        if choice == '0':
          print("메뉴화면으로 돌아갑니다.\n")
          break
        elif choice == '1':
          print(f"{name} 학생의 현재 국어 점수 : {stu[2]}")
          stu[2] = int(input("국어 점수 수정 입력 >> "))
        elif choice == '2':
          print(f"{name} 학생의 현재  영어 점수 : {stu[3]}")
          stu[3] = int(input("영어 점수 수정 입력 >> "))
        elif choice == '3':
          print(f"{name} 학생의 현재 수학 점수 : {stu[4]}")
          stu[4] = int(input("수학 점수 수정 입력 >> "))

        stu[5] = stu[2] + stu[3] + stu[4]
        stu[6] = stu[5] / 3

        print("수정이 완료되었습니다.\n")

    if chk == 0:
      print("수정하려는 학생이 존재하지 않습니다.\n")    

  elif choice == '4':
    print("[ 학생성적검색 ]\n"); chk = 0

    name = input("검색하려는 학생 이름 입력 >> ")
    for stu in students:
      if name == stu[1]:
        print(f"{name} 학생을 찾았습니다.\n"); chk = 1
        for t in title:
          print("{}".format(t), end="\t")
        print(); print("-" * 60)
        print(f"{stu[0]}\t{stu[1]}\t{stu[2]}\t{stu[3]}\t{stu[4]}\t{stu[5]}\t{stu[6]:.2f}\t{stu[7]}\n")

    if chk == 0:
      print("검색하려는 학생이 존재하지 않습니다.\n")

  elif choice == '5':
    print("[ 학생성적삭제 ]\n")

    for idx, stu in students:
      pass
  elif choice == '6':
    print("[ 학생등수처리 ]\n")
    pass
