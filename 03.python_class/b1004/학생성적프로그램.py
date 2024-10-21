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
      name = input(f"{no}번째 학생 이름 입력(메뉴화면: 0) >> ")
      if name == '0':
        print("메뉴화면으로 이동합니다.\n")
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
    
    for title in s_title:
      print(title, end='\t')
    print(); print('-' * 60)

    for s_out in students:
      print(f"{s_out[0]}\t{s_out[1]}\t{s_out[2]}\t{s_out[3]}\t{s_out[4]}\t{s_out[5]}\t{s_out[6]:.2f}\t{s_out[7]}")
    print()
  elif choice == '3':
    print("[ 학생성적수정 ]")
    name = input("수정하려는 학생이름 입력 >> ")
    cnt = 0
    for search in students:
      if name == search[1]:
        print(f"{name} 학생을 찾았습니다.")
        cnt = 1
        print("[ 과목선택 ]")
        print("0. 메뉴화면")
        print("1. 국어점수")
        print("2. 영어점수")
        print("3. 수학점수")
        choice = input("원하는 번호를 입력하세요.>> ")

        if choice == '1':
          print("현재 국어 점수 :", search[2])
          search[2] = int(input("국어점수 수정 입력 >> "))
        elif choice == '2':
          print("현재 영어 점수 :", search[3])
          search[3] = int(input("영어점수 수정 입력 >> "))
        elif choice == '3':
          print("현재 수학 점수 :", search[4])
          search[4] = int(input("수학점수 수정 입력 >> "))
        elif choice == '0':
          print("메뉴화면으로 이동합니다.\n")
          cnt = 1
          break
        if choice != '0':
          search[5] = search[2] + search[3] + search[4] # 합계변경
          search[6] = search[5] / 3 # 평균변경
          print(f"{name} 학생의 성적을 수정하였습니다.\n")
    # 없을 경우
    if cnt == 0:
      print("수정하고자 하는 학생 이름이 없습니다."); print()
  elif choice == '4':
    print("[ 학생성적검색 ]")
    name = input("검색하려는 학생이름 입력 >> ")
    cnt = 0
    for search in students:
      if name == search[1]:
        print(f"{name} 학생을 찾았습니다.")
        cnt = 1
        for title in s_title:
          print(title, end='\t')
        print(); print('-' * 60)
        print(f"{search[0]}\t{search[1]}\t{search[2]}\t{search[3]}\t{search[4]}\t{search[5]}\t{search[6]:.2f}\t{search[7]}"); print()
        break
    if cnt == 0:
      print("찾고자하는 학생의 이름이 없습니다.\n")