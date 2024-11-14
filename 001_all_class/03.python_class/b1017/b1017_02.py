subject = ['이름', '국어', '영어', '수학', '합계', '평균']
students = []

########## 함수 선언 ##########
def stuScore_update(subject, choice, s, keys):
  print(f"현재 {subject[choice]}점수 :", s[keys[choice]])
  s[keys[choice]] = int(input("변경점수를 입력하세요.>> "))
# -------------------------- #
while True:
  print("1. 학생성적 입력")
  print("2. 학생성적 출력")
  print("3. 학생성적 수정")
  choice = int(input("원하는 번호를 입력하세요.>> "))
  if choice == 1:
    name = input("학생의 이름을 입력하세요.>> ")
    score = []; sum = 0
    for i in range(3):
      score.append(int(input(f"{subject[i + 1]}점수를 입력하세요.>> ")))
      sum += score[i]
    avg = sum / len(score)
    s = {'name': name, 'kor': score[0], 'eng': score[1], 'math': score[2], 'total': sum, 'avg': avg}
    students.append(s)
    print(students)
  elif choice == 3:
    search = input("찾으려는 학생의 이름을 입력하세요.>> ")
    for s in students:
      if s['name'] == search:
        print("[ 수정과목 선택 ]")
        print("1. 국어\t2.영어\t3.수학\t0.이전화면이동")
        choice = int(input("원하는 번호를 입력하세요.>> "))
        keys = list(s.keys())
        if choice == 1:
          stuScore_update(subject, choice, s, keys)
        elif choice == 2:
          stuScore_update(subject, choice, s, keys)
        elif choice == 3:
          stuScore_update(subject, choice, s, keys)
        elif choice == 0:
          print("이전화면으로 이동합니다.")
          break