students = [] # 학생들을 담을 리스트
stu = {} # 각각의 학생을 담을 딕셔너리
score = [] # 학생 성적을 담을 리스트
no, total, avg, rank = 0, 0, 0, 0 # 학생정보 저장 변수
name = "" # 학생이름 변수
choice = "" # 번호선택 변수
chk = 0 # 성공여부 체크 변수
cnt = 0 # 등수처리용 변수
title = ['번호', '이름', '국어', '영어', '수학', '합계', '평균', '등수'] # 제목 리스트

while True:
  print("[ 학생성적프로그램 ]\n")
  print("-" * 60)
  print("0. 프로그램종료")
  print("1. 학생성적입력")
  print("2. 학생성적출력")
  print("3. 학생성적검색")
  print("4. 학생성적수정")
  print("5. 학생성적삭제")
  print("6. 학생등수처리")
  print("7. 학생성적정렬")
  print("-" * 60); print()

  choice = input("원하는 번호 입력 >> ")
  if choice == '0':
    print("[ 프로그램종료 ]")
    print("프로그램을 종료합니다.")
    break
  elif choice == '1':
    print("[ 학생성적입력 ]\n")
    
    while True:
      no = len(students) + 1
      name = input(f"{no}번째 학생이름 입력(0: 메뉴화면) >> ")
      if name == '0':
        print("메뉴화면으로 돌아갑니다.\n")
        break
      for i in range(3): # 국어, 영어, 수학 점수 입력
        score.insert(i, int(input(f"{title[i + 2]}점수 입력 >> ")))
        total += score[i]
      avg = total / 3
      rank = 0

      stu = {'no': no, 'name': name, 'kor': score[0], 'eng': score[1], 'math': score[2], 'total': total, 'avg': avg, 'rank': rank}
      students.append(stu)

      print(f"{name} 학생이 저장되었습니다.\n")
      total = 0 # 다음 학생의 점수합계를 저장하기 위해 초기화

  elif choice == '2':
    print("[ 학생성적출력 ]\n")

    for s_t in title: # 상단 제목 출력
      print(s_t, end="\t")
    print(); print("-" * 60)

    for s in students:
      print(f"{s['no']}\t{s['name']}\t{s['kor']}\t{s['eng']}\t{s['math']}\t{s['total']}\t{s['avg']:.2f}\t{s['rank']}")
    print()

  elif choice == '3':
    print("[ 학생성적검색 ]\n")

    name = input("검색하려는 학생이름 입력 >> "); chk = 0
    for s in students:
      if name == s['name']:
        print(f"{name} 학생을 찾았습니다.\n"); chk = 1

        for s_t in title: # 상단 제목 출력
          print(s_t, end="\t")
        print(); print("-" * 60)

        print(f"{s['no']}\t{s['name']}\t{s['kor']}\t{s['eng']}\t{s['math']}\t{s['total']}\t{s['avg']:.2f}\t{s['rank']}\n")

    # 학생이 없을 경우
    if chk == 0:
      print(f"{name} 학생이 존재하지 않습니다.\n")

  elif choice == '4':
    print("[ 학생성적수정 ]\n")

    name = input("수정하려는 학생이름 입력 >> "); chk = 0
    for s in students:
      if name == s['name']:
        print(f"{name} 학생을 찾았습니다. \n"); chk = 1

        print("-" * 30)
        print("0. 메뉴화면")
        print("1. 국어점수")
        print("2. 영어점수")
        print("3. 수학점수")
        print("-" * 30); print()

        choice = input("원하는 번호 입력 >> ")
        if choice == '0':
          print("메뉴화면으로 돌아갑니다.\n")
          break
        elif choice == '1':
          print(f"{name} 학생의 현재 국어 점수 : {s['kor']}")
          s['kor'] = int(input(f"{name} 학생의 국어점수 수정 입력 >> "))
        elif choice == '2':
          print(f"{name} 학생의 현재 국어 점수 : {s['eng']}")
          s['eng'] = int(input(f"{name} 학생의 영어점수 수정 입력 >> "))
        elif choice == '3':
          print(f"{name} 학생의 현재 국어 점수 : {s['math']}")
          s['math'] = int(input(f"{name} 학생의 수학점수 수정 입력 >> "))
        
        s['total'] = s['kor'] + s['eng'] + s['math']
        s['avg'] = s['total'] / 3

        print(f"{name} 학생의 점수가 수정되었습니다.\n")
    
    # 학생이 없을 경우
    if chk == 0:
      print(f"{name} 학생이 존재하지 않습니다.\n")
  
  elif choice == '5':
    print("[ 학생성적삭제 ]\n")

    name = input("삭제하려는 학생이름 입력 >> "); chk = 0
    for idx, s in enumerate(students):
      if name == s['name']:
        print(f"{name} 학생을 찾았습니다.\n"); chk = 1

        print("※  주의 ※")
        answer = input(f"{name} 학생을 삭제하시겠습니까?(y or n) >> ")
        if answer == 'y':
          del students[idx]
          print(f"{name} 학생이 삭제되었습니다.\n")
        elif answer == 'n':
          print("삭제를 취소하였습니다.\n")
        else:
          print("잘못된 문자를 입력하였습니다.\n")
    
    # 학생이 없을 경우
    if chk == 0:
      print(f"{name} 학생이 존재하지 않습니다.\n")

  elif choice == '6':
    print("[ 학생등수처리 ]\n")

    for s in students:
      cnt = 1
      for s2 in students:
        if s['total'] < s2['total']:
          cnt += 1
      s['rank'] = cnt
    
    print("등수처리가 완료되었습니다.\n")
  
  elif choice == '7':
    print("[ 학생성적정렬 ]\n")

    print("-" * 30)
    print("1. 이름 오름차순")
    print("2. 이름 내림차순")
    print("3. 합계 오름차순")
    print("4. 합계 내림차순")
    print("5. 번호 오름차순")
    print("-" * 30); print()

    choice = input("원하는 번호 입력 >> ")
    if choice == '1':
      students.sort(key=lambda x: x['name'])
    elif choice == '2':
      students.sort(key=lambda x: x['name'], reverse=True)
    elif choice == '3':
      students.sort(key=lambda x: x['total'])
    elif choice == '4':
      students.sort(key=lambda x: x['total'], reverse=True)
    elif choice == '5':
      students.sort(key=lambda x: x['no'])
    else:
      print("잘못된 번호 입력")

    print("정렬이 완료되었습니다.\n")