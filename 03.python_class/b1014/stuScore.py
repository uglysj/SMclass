students = [
  {'no': 1, 'name': "홍길동", 'kor': 100, 'eng': 100, 'math': 99, 'total': 299, 'avg': 99.67, 'rank': 0},
  {'no': 2, 'name': "유관순", 'kor': 80, 'eng': 80, 'math': 85, 'total': 245, 'avg': 81.67, 'rank': 0},
  {'no': 3, 'name': "이순신", 'kor': 90, 'eng': 90, 'math': 91, 'total': 271, 'avg': 90.33, 'rank': 0},
  {'no': 4, 'name': "강감찬", 'kor': 60, 'eng': 65, 'math': 67, 'total': 192, 'avg': 64.00, 'rank': 0},
  {'no': 5, 'name': "김구", 'kor': 100, 'eng': 100, 'math': 84, 'total': 284, 'avg': 94.67, 'rank': 0}
]
# students = []
stuNo = len(students) # 학생번호 생성 / 리스트에 학생이 있으면, 그 인원으로 변경
s_title = ['번호', '이름', '국어', '영어', '수학', '합계', '평균', '등수']
choice = "" # 원하는 번호 입력 변수
chk = 0 # 체크변수
cnt = 1 # 성적처리
no, kor, eng, math, total, avg, rank = 0, 0, 0, 0, 0, 0, 0 # 성적처리 변수
name = "" # 학생이름 변수

# 메뉴출력함수 시작
def title_program():
  print("[ 학생성적 프로그램 ]")
  print("-" * 60)
  print("0. 프로그램종료")
  print("1. 학생성적입력")
  print("2. 학생성적출력")
  print("3. 학생성적수정")
  print("4. 학생성적검색")
  print("5. 학생성적삭제")
  print("6. 학생등수처리")
  print("7. 학생성적정렬")
  print("-" * 60)
  choice = input("원하는 번호를 입력하세요.>> ")
  return choice
# -----------------------------------------------------

# 학생성적입력함수 시작 - 일반변수 변경
def stu_input(stuNo):
  print("[ 학생성적입력 ]\n")
  while True:
    # 학생성적 직접 입력
    no = stuNo + 1
    name = input(f"{no}번째 학생 이름 입력(0: 메뉴화면) >> ")
    if name == '0':
      print("성적입력을 취소합니다.\n")
      break
    kor = int(input("국어 점수 입력 >> "))
    eng = int(input("영어 점수 입력 >> "))
    math = int(input("수학 점수 입력 >> "))
    total = kor + eng + math
    avg = total / 3
    rank = 0

    ss = {'no': no, 'name': name, 'kor': kor, 'eng': eng, 'math': math, 'total': total, 'avg': avg, 'rank': rank}
    students.append(ss)
    stuNo += 1 # 학생 수 증가
    print(f"{name} 학생의 성적이 저장되었습니다.\n")
    
  return stuNo
# -----------------------------------------------------

while True:
  choice = title_program() # 메뉴출력함수 호출
  
  if choice == '0':
    print("[ 프로그램종료 ]")
    print("프로그램을 종료합니다.")
    break
  elif choice == '1':
    stuNo = stu_input(stuNo) # 학생성적입력함수 호출
  elif choice == '2':
    print("[ 학생성적출력 ]\n")

    for t in s_title:
      print("{}".format(t), end="\t")
    print(); print("-" * 60)

    for stu in students:
      print(f"{stu['no']}\t{stu['name']}\t{stu['kor']}\t{stu['eng']}\t{stu['math']}\t{stu['total']}\t{stu['avg']:.2f}\t{stu['rank']}")
    print()

  elif choice =='3':
    print("[ 학생성적수정 ]\n")

    name = input("수정하려는 학생 이름 입력 >> "); chk = 0
    for stu in students:
      if name == stu['name']:
        print(f"{name} 학생을 찾았습니다.\n"); chk = 1

        print("-" * 30)
        print("0. 메뉴화면")
        print("1. 국어점수")
        print("2. 영어점수")
        print("3. 수학점수")
        print("-" * 30)
        choice = input("원하는 번호를 선택하세요.>> ")

        if choice == '0':
          print("메뉴화면으로 돌아갑니다.\n")
          break
        elif choice == '1':
          print(f"{name} 학생의 현재 국어점수 : {stu['kor']}")
          stu['kor'] = int(input(f"{name} 학생의 국어점수 수정입력 >> "))
        elif choice == '2':
          print(f"{name} 학생의 현재 영어점수 : {stu['eng']}")
          stu['eng'] = int(input(f"{name} 학생의 영어점수 수정입력 >> "))
        elif choice == '3':
          print(f"{name} 학생의 현재 수학점수 : {stu['math']}")
          stu['math'] = int(input(f"{name} 학생의 수학점수 수정입력 >> "))
        
        stu['total'] = stu['kor'] + stu['eng'] + stu['math']
        stu['avg'] = stu['total'] / 3

        print("수정이 완료되었습니다.\n")
    
    if chk == 0:
      print("수정하려는 학생의 이름이 없습니다.\n")

  elif choice == '4':
    print("[ 학생성적검색 ]\n")

    name = input("검색하려는 학생 이름 입력 >> ")
    for stu in students:
      if name == stu['name']:
        print(f"{name} 학생을 찾았습니다.\n")

        for t in s_title:
          print("{}".format(t), end="\t")
        print(); print("-" * 60)

        print(f"{stu['no']}\t{stu['name']}\t{stu['kor']}\t{stu['eng']}\t{stu['math']}\t{stu['total']}\t{stu['avg']:.2f}\t{stu['rank']}\n")

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
    while True:
      print("[ 학생성적정렬 ]\n")

      print("-" * 40)
      print("0. 메인메뉴")
      print("1. 이름 내림차순")
      print("2. 이름 오름차순")
      print("3. 합계 내림차순")
      print("4. 합계 오름차순")
      print("5. 번호 내림차순")
      print("-" * 40)
      choice = input("원하는 번호를 입력하세요.>> ")

      if choice == '0':
        print("메인메뉴로 이동합니다.\n")
        break
      elif choice == '1':
        students.sort(key= lambda x: x['name'])
      elif choice == '2':
        students.sort(key= lambda x: x['name'], reverse=True)
      elif choice == '3':
        students.sort(key= lambda x: x['total'])
      elif choice == '4':
        students.sort(key= lambda x: x['total'], reverse=True)
      
      print("정렬이 완료되었습니다.\n")