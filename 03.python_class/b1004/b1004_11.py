students = []
no = 1
s_title = ['번호', '이름', '국어', '영어', '수학', '합계', '평균', '등수']

# 학생성적프로그램
while True:
  print("[ 학생성적프로그램 ]")
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
    print("[ 학생성적입력 ]")
    
    while True:
      name = input("학생 이름 입력(메뉴화면: 0) >> ")
      if name == '0':
        print("메뉴화면으로 이동합니다.")
        break
      kor = int(input("국어 점수 입력 >> "))
      eng = int(input("영어 점수 입력 >> "))
      math = int(input("수학 점수 입력 >> "))
      total = kor + eng + math
      avg = total / 3
      rank = 0

      print(f"번호: {no}, 이름: {name}, 국어: {kor}, 영어: {eng}, 수학: {math}, 합계: {total}, 평균: {avg:.2f}")
      students.append([no, name, kor, eng, math, total, avg, rank])
      no += 1
  elif choice == '2':
    print("[ 학생성적출력 ]")
    
    for s_t in s_title:
      print(s_t, end='\t')
    print(); print('-' * 60)
    for stu in students:
      print(f"{stu[0]}\t{stu[1]}\t{stu[2]}\t{stu[3]}\t{stu[4]}\t{stu[5]}\t{stu[6]:.2f}\t{stu[7]}")
    print()
  elif choice == '3':
    print("[ 학생성적수정 ]")
    
    cnt = 0 # 성공 여부 체크
    name = input("수정하고자 하는 학생 이름 입력 >> ")
    for stu in students:
      if name == stu[1]:
        print(f"{name} 학생을 찾았습니다.")
        cnt = 1

        print("0. 메뉴화면")
        print("1. 국어점수")
        print("2. 영어점수")
        print("3. 수학점수")
        
        choice = input("원하는 번호를 입력하세요.>> ")
        if choice == '0':
          print("메뉴화면으로 이동합니다.\n")
          break
        elif choice == '1':
          print(f"{name} 학생의 국어 점수 : {stu[2]}")
          stu[2] = int(input("국어 점수 수정 입력 >> "))
        elif choice == '2':
          print(f"{name} 학생의 영어 점수 : {stu[3]}")
          stu[3] = int(input("국어 점수 수정 입력 >> "))
        elif choice == '3':
          print(f"{name} 학생의 수학 점수 : {stu[4]}")
          stu[4] = int(input("국어 점수 수정 입력 >> "))

        stu[5] = stu[2] + stu[3] + stu[4]
        stu[6] = stu[5] / 3
        print("수정이 완료되었습니다.\n")

    # 없을경우
    if cnt == 0:
      print("수정하려고 하는 학생이 없습니다.\n")
  elif choice == '4':
    print("[ 학생성적검색 ]")
    
    cnt = 0 # 성공 여부 체크
    name = input("검색하고자 하는 학생 이름 입력 >> ")
    for stu in students:
      if name == stu[1]:
        print(f"{name} 학생을 찾았습니다.")
        cnt = 1
        for s_t in s_title:
          print(s_t, end='\t')
        print(); print('-' * 60)
        print(f"{stu[0]}\t{stu[1]}\t{stu[2]}\t{stu[3]}\t{stu[4]}\t{stu[5]}\t{stu[6]:.2f}\t{stu[7]}"); print() # 찾는학생 한명만 출력
        break

    # 없을경우
    if cnt == 0:
      print("검색하고자 하는 학생이 없습니다.\n")

  elif choice == '5':
    print("[ 학생성적삭제 ]")

    cnt = 0 # 성공 여부 체크
    name = input("삭제하고자 하는 학생 이름 입력 >> ")
    for idx, stu in enumerate(students):
      if name == stu[1]:
        print(f"{name} 학생을 찾았습니다.")
        cnt = 1
        
        answer = input(f"{name}학생을 삭제하시겠습니까?(y or n) >> ")
        if answer == 'y':
          del students[idx]
          print("삭제를 완료하였습니다.\n")
        elif answer == 'n':
          print("삭제를 취소합니다.\n")

    # 없을경우
    if cnt == 0:
      print("삭제하고자 하는 학생이 없습니다.")