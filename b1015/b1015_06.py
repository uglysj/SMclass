students = [
  {'no': 1, 'name': "홍길동", 'kor': 100, 'eng': 100, 'math': 99, 'total': 299, 'avg': 99.67, 'rank': 0},
  {'no': 2, 'name': "김관순", 'kor': 80, 'eng': 80, 'math': 85, 'total': 245, 'avg': 81.67, 'rank': 0},
  {'no': 3, 'name': "이순동", 'kor': 90, 'eng': 90, 'math': 91, 'total': 271, 'avg': 90.33, 'rank': 0},
  {'no': 4, 'name': "강홍찬", 'kor': 60, 'eng': 65, 'math': 67, 'total': 192, 'avg': 64.00, 'rank': 0},
  {'no': 5, 'name': "김구길", 'kor': 100, 'eng': 100, 'math': 84, 'total': 284, 'avg': 94.67, 'rank': 0}
]
s_title = ['번호', '이름', '국어', '영어', '수학', '합계', '평균', '등수']
choice = ""

print("[ 학생성적삭제 ]\n")
name = input("삭제하려는 학생이름 입력 >> "); chk = 0
for idx, s in enumerate(students):
  if s['name'] == name:
    chk = 1
    print("※  주의 ※")
    answer = input(f"{name} 학생을 삭제하시겠습니까?(y or n) >> ")
    if answer == 'y':
      del students[idx]
      print(f"{name} 학생이 삭제되었습니다.\n")
    elif answer == 'n':
      print("삭제를 취소하였습니다.\n")
      break
    else:
      print("잘못된 문자를 입력하였습니다.\n")

if chk == 0:
  print(f"{name} 학생이 존재하지 않습니다.\n")
# else:
#   stu_output(s_title, students)