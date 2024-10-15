students = [
  {'no': 1, 'name': "홍길동", 'kor': 100, 'eng': 100, 'math': 99, 'total': 299, 'avg': 99.67, 'rank': 0},
  {'no': 2, 'name': "유관순", 'kor': 80, 'eng': 80, 'math': 85, 'total': 245, 'avg': 81.67, 'rank': 0},
  {'no': 3, 'name': "이순신", 'kor': 90, 'eng': 90, 'math': 91, 'total': 271, 'avg': 90.33, 'rank': 0},
  {'no': 4, 'name': "강감찬", 'kor': 60, 'eng': 65, 'math': 67, 'total': 192, 'avg': 64.00, 'rank': 0},
  {'no': 5, 'name': "김구", 'kor': 100, 'eng': 100, 'math': 84, 'total': 284, 'avg': 94.67, 'rank': 0}
]
stuNo = len(students) # 학생번호 생성 / 리스트에 학생이 있으면, 그 인원으로 변경
s_title = ['번호', '이름', '국어', '영어', '수학', '합계', '평균', '등수']
choice = "" # 원하는 번호 입력 변수
chk = 0 # 체크변수
cnt = 1 # 성적처리
no, kor, eng, math, total, avg, rank = 0, 0, 0, 0, 0, 0, 0 # 성적처리 변수
name = "" # 학생이름 변수

############## 함수 선언 ################
########## 1. 학생성적입력함수 ##########
def stu_input(stuNo, students):
  print("[ 학생성적입력 ]\n")

  while True:
    no = stuNo + 1
    name = input(f"{no}번째 학생이름 입력(0. 이전화면) >> ")
    if name == '0':
      print("이전화면으로 돌아갑니다.\n")
      break
    score = []; total = 0
    for i in range(3):
      score.append(int(input(f"{s_title[i + 2]}점수 입력 >> ")))
      total += score[i]
    avg = total / 3
    rank = 0

    students.append({'no': no, 'name': name, 'kor': score[0], 'eng': score[1], 'math': score[2], 'total': total, 'avg': avg, 'rank': rank})
    stuNo += 1

    print(f"{name} 학생의 성적이 입력되었습니다.\n")
#######################################
########## 2. 학생성적출력함수 ##########
def stu_output(students):
  print("[ 학생성적출력 ]\n")

  for t in s_title:
    print(t, end='\t')
  print(); print("-" * 60)

  for stu in students:
    print(f"{stu['no']}\t{stu['name']}\t{stu['kor']}\t{stu['eng']}\t{stu['math']}\t{stu['total']}\t{stu['avg']:.2f}\t{stu['rank']}")
  print()
#######################################
########## 3. 학생성적수정함수 ##########
def stu_update(students):
  print("[ 학생성적수정 ]\n")

  name = input("수정하려는 학생 이름 입력 >> "); chk = 0
  for stu in students:
    if name == stu['name']:
      print(f"{name} 학생을 찾았습니다.\n"); chk = 1
      print("[ 수정 과목 선택 ]"); print("-" * 30)
      print("1. 국어점수"); print("2. 영어점수"); print("3. 수학점수"); print("0. 이전화면"); print("-" * 30)
      choice = input("원하는 번호를 입력하세요.>> ")

      if choice == '1':
        print(f"현재 {name} 학생의 국어점수 : {stu['kor']}")
        stu['kor'] = int(input("수정 국어점수 입력 >> "))
      elif choice == '2':
        print(f"현재 {name} 학생의 영어점수 : {stu['eng']}")
        stu['eng'] = int(input("수정 영어점수 입력 >> "))
      elif choice == '3':
        print(f"현재 {name} 학생의 수학점수 : {stu['math']}")
        stu['math'] = int(input("수정 수학점수 입력 >> "))
      elif choice == '0':
        print("이전화면으로 돌아갑니다.\n")
        break

      stu['total'] = stu['kor'] + stu['eng'] + stu['math']
      stu['avg'] = stu['total'] / 3

      print(f"{name} 학생의 점수가 수정되었습니다.\n")
      stu_output([stu])

  if chk == 0:
    print(f"{name} 학생은 존재하지 않습니다.\n")
#######################################
########## 4. 학생성적검색함수 ##########
def stu_search(students):
  print("[ 학생성적검색 ]\n")

  while True:
    chk = 0
    name = input("검색하려는 학생 이름 입력(0. 이전화면 이동) >> ")
    if name == '0':
      print("이전화면으로 이동합니다.\n")
      break

    sArr = []
    for stu in students:
      if stu['name'].find(name) != -1:
        sArr.append(stu)
        chk = 1
    
    if chk == 0:
      print(f"{name} 학생은 존재하지 않습니다.\n")
    else:
      print(f"{name} 이라는 이름으로 {len(sArr)}명 검색되었습니다.\n")
      stu_output(sArr)
#######################################
########## 5. 학생성적삭제함수 ##########
def stu_delete(students):
  print("[ 학생성적삭제 ]\n")

  chk = 0; name = input("삭제하려는 학생이름 입력 >> ")
  for idx, stu in enumerate(students):
    if name == stu['name']:
      print(f"{name} 학생을 찾았습니다.\n"); chk = 1
      
      print("※  주의 ※")
      answer = input(f"{name} 학생을 삭제하시겠습니까?(y or n) >> ")
      sArr = []
      if answer == 'y':
        sArr.append(stu)
        del students[idx]
        print(f"{name} 학생이 삭제되었습니다.\n")
      elif answer == 'n':
        print("삭제를 취소하였습니다.\n")
      else:
        print("잘못입력하셨습니다.\n")
  
  if chk == 0:
    print(f"{name} 학생은 존재하지 않습니다.\n")
  else:
    stu_output(sArr)
#######################################
########## 6. 학생등수처리함수 ##########
def stu_rank(students):
  print("[ 학생등수처리 ]\n")

  for i in students:
    cnt = 1
    for j in students:
      if i['total'] < j['total']:
        cnt += 1
    i['rank'] = cnt
  
  print("등수처리가 완료되었습니다.\n")
#######################################
########################################

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
  print("7. 학생성적정렬")
  print("-" * 60)
  choice = input("원하는 번호를 입력하세요.>> ")

  if choice == '1':
    stuNo = stu_input(stuNo, students)
  elif choice == '2':
    stu_output(students)
  elif choice == '3':
    stu_update(students)
  elif choice == '4':
    stu_search(students)
  elif choice == '5':
    stu_delete(students)
  elif choice == '6':
    stu_rank(students)
  elif choice == '0':
    print("[ 프로그램종료 ]")
    print("프로그램을 종료합니다.")
    break