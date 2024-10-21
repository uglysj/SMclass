students = []
s_title = ['번호', '이름', '국어', '영어', '수학', '합계', '평균', '등수']
choice = "" # 원하는 번호 입력 변수
stuNo = len(students) # 학생번호 생성 / 리스트에 학생이 있으면, 그 인원으로 변경
chk = 0 # 체크변수
cnt = 1 # 성적처리
no, kor, eng, math, total, avg, rank = 0, 0, 0, 0, 0, 0, 0 # 성적처리 변수
name = "" # 학생이름 변수

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
      # 학생성적 직접 입력
      no = stuNo + 1
      name = input(f"{no}번째 학생 이름 입력(0: 메뉴화면) >> ")
      if name == '0':
        print("성적입력을 취소합니다.")
        break
      kor = int(input("국어 점수 입력 >> "))
      eng = int(input("영어 점수 입력 >> "))
      math = int(input("수학 점수 입력 >> "))
      total = kor + eng + math
      avg = total / 3
      rank = 0

      students.append([no, name, kor, eng, math, total, avg, rank])
      stuNo += 1 # 학생 수 증가
      print(f"{name} 학생의 성적이 저장되었습니다.\n")

  elif choice == '2':
    print("[ 학생성적출력 ]\n")
    # 상단타이틀 출력
    for title in s_title:
      print(f"{title}", end='\t')
    print()
    print("-" * 60)
    
    # 학생출력
    for st in students:
      print(f"{st[0]}\t{st[1]}\t{st[2]}\t{st[3]}\t{st[4]}\t{st[5]}\t{st[6]:.2f}\t{st[7]}")
    print()

  elif choice == '3':
    print("[ 학생성적수정 ]\n")
    name = input("찾고자하는 학생의 이름을 입력하세요. >> "); cnt = 0
    for st in students:
      if name == st[1]:
        print(f"{name} 학생을 찾았습니다.\n"); cnt = 1
        print("[ 수정하고자 하는 과목 선택 ]")
        print("0. 메뉴화면")
        print("1. 국어점수")
        print("2. 영어점수")
        print("3. 수학점수")
        choice = input("원하는 번호를 입력하세요. >> ")

        if choice == '0':
          print("성적 수정을 취소합니다.\n")
          break
        elif choice == '1':
          print(f"{name} 학생의 현재 국어 점수 : {st[2]}")
          st[2] = int(input("국어 점수 수정 입력 >> "))
        elif choice == '2':
          print(f"{name} 학생의 현재 영어 점수 : {st[3]}")
          st[3] = int(input("영어 점수 수정 입력 >> "))
        elif choice == '3':
          print(f"{name} 학생의 현재 수학 점수 : {st[4]}")
          st[4] = int(input("수학 점수 수정 입력 >> "))
        else:
          print("잘못된 번호가 입력되었습니다.\n")
          break;
        
        # 수정 점수 합계 및 평균
        st[5] = st[2] + st[3] + st[4]
        st[6] = st[5] / 3
        print(f"{name} 학생의 성적이 수정되었습니다.\n")    

    # 학생 있는지 검사
    if cnt == 0:
      print("{} 학생이 없습니다.\n".format(name))

  elif choice == '4':
    print("[ 학생성적검색 ]\n")

    name = input("찾고자하는 학생의 이름을 입력하세요. >> "); chk = 0
    for st in students:
      if name == st[1]:
        print(f"{name} 학생을 찾았습니다.\n"); chk = 1
        # 상단타이틀 출력
        for title in s_title:
          print(f"{title}", end='\t')
        print(); print("-" * 60)
        
        # 학생출력
        print(f"{st[0]}\t{st[1]}\t{st[2]}\t{st[3]}\t{st[4]}\t{st[5]}\t{st[6]:.2f}\t{st[7]}\n")

    # 모든 학생 비교가 끝난 후, chk
    if chk == 0:
      print(f"{name} 학생이 없습니다.\n")

  elif choice == '5':
    print("[ 학생성적삭제 ]\n")
    
    name = input("삭제하고자 하는 학생 이름 입력 >> "); chk = 0
    for idx, stu in enumerate(students):
      if name == stu[1]:
        print(f"{name} 학생을 찾았습니다.\n"); chk = 1
        
        print("※  주의※\n삭제시 복구 불가능")
        answer = input(f"{name} 학생을 삭제하시겠습니까?(y or n) >> ")
        if answer == 'y':
          del students[idx]
          print("삭제를 완료하였습니다.\n")
        elif answer == 'n':
          print("삭제를 취소합니다.\n")
          break

    # 없을경우
    if chk == 0:
      print("삭제하고자 하는 학생이 없습니다.\n")

  elif choice == '6':
    print("[ 학생등수처리 ]\n")

    for s in students:
      cnt = 1
      for st in students:
         if s[5] < st[5]:
           cnt += 1
      s[7] = cnt # 등수입력
    
    print("등수처리가 완료되었습니다.\n")