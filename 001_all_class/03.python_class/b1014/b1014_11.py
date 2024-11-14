students = [
  {'no': 1, 'name': "홍길동", 'kor': 100, 'eng': 100, 'math': 99, 'total': 299, 'avg': 99.67, 'rank': 0},
  {'no': 2, 'name': "유관순", 'kor': 80, 'eng': 80, 'math': 85, 'total': 245, 'avg': 81.67, 'rank': 0},
  {'no': 3, 'name': "이순신", 'kor': 90, 'eng': 90, 'math': 91, 'total': 271, 'avg': 90.33, 'rank': 0},
  {'no': 4, 'name': "강감찬", 'kor': 60, 'eng': 65, 'math': 67, 'total': 192, 'avg': 64.00, 'rank': 0},
  {'no': 5, 'name': "김구", 'kor': 100, 'eng': 100, 'math': 84, 'total': 284, 'avg': 94.67, 'rank': 0}
]
stuNo = len(students)
s_title = ['번호', '이름', '국어', '영어', '수학', '합계', '평균', '등수']

##### 학생성적입력 함수 시작 #####
def stu_input(stuNo, students, s_title):
  while True:
    no = stuNo + 1
    name = input(f"{no}번째 학생이름 입력(0. 이전화면) >> ")
    if name == '0':
      break
    score = []
    total = 0
    for i in range(3):
      score.append(int(input(f"{s_title[i + 2]} 점수 입력 >> ")))
      total += score[i]
    avg = total / 3
    rank = 0

    students.append({'no': no, 'name': name, 'kor': score[0], 'eng': score[1], 'math': score[2], 'total': total, 'avg': avg, 'rank': rank})
    stuNo += 1
  return stuNo
##### 학생성적입력 함수 끝 #####

##### 학생성적출력 함수 시작 #####
def stu_output(s_title, students):
  print("[ 학생성적출력 ]\n")

  for t in s_title:
    print("{}".format(t), end="\t")
  print(); print("-" * 60)

  for stu in students:
    print(f"{stu['no']}\t{stu['name']}\t{stu['kor']}\t{stu['eng']}\t{stu['math']}\t{stu['total']}\t{stu['avg']:.2f}\t{stu['rank']}")
  print()
##### 학생성적출력 함수 끝 #####

# 학생성적입력 함수 호출
stuNo = stu_input(stuNo, students, s_title)

# 학생성적출력 함수 호출
stu_output(s_title, students)