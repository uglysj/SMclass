students = [
  {'no': 1, 'name': "홍길동", 'kor': 100, 'eng': 100, 'math': 99, 'total': 299, 'avg': 99.67, 'rank': 0},
  {'no': 2, 'name': "유관순", 'kor': 80, 'eng': 80, 'math': 85, 'total': 245, 'avg': 81.67, 'rank': 0},
  {'no': 3, 'name': "이순신", 'kor': 90, 'eng': 90, 'math': 91, 'total': 271, 'avg': 90.33, 'rank': 0},
  {'no': 4, 'name': "강감찬", 'kor': 60, 'eng': 65, 'math': 67, 'total': 192, 'avg': 64.00, 'rank': 0},
  {'no': 5, 'name': "김구", 'kor': 100, 'eng': 100, 'math': 84, 'total': 284, 'avg': 94.67, 'rank': 0}
]
s_title = ['번호', '이름', '국어', '영어', '수학', '합계', '평균', '등수']
stuNo = len(students) # 학생번호 생성 / 리스트에 학생이 있으면, 그 인원으로 변경
choice = "" # 원하는 번호 입력 변수
chk = 0 # 체크변수
cnt = 1 # 성적처리
no, kor, eng, math, total, avg, rank = 0, 0, 0, 0, 0, 0, 0 # 성적처리 변수
name = "" # 학생이름 변수

# 학생성적입력 함수 선언
def stu_input(stuNo, s_title, students):
  while True:
    print("[ 학생성적입력 ]")
    no = stuNo + 1
    name = input(f"{no}번째 학생이름 입력(0. 이전화면 이동) >> ")
    if name == '0':
      print("이전화면으로 이동합니다.\n")
      break
    score = []
    total = 0
    for i in range(3):
      score.append(int(input(f"{s_title[i + 2]}점수 입력 >> ")))
      total += score[i]
    avg = total / 3
    rank = 0

    s = {'no': no, 'name': name, 'kor': score[0], 'eng': score[1], 'math': score[2], 'total': total, 'avg': avg, 'rank': rank}
    students.append(s)
    stuNo += 1
    print(f"{name} 학생성적이 저장되었습니다.\n")

    print(students)
  return stuNo

##### 실제 프로그램 시작 부분 #####
choice = input("원하는 번호 입력 >> ")

if choice == '1':
  stuNo = stu_input(stuNo, s_title, students)
  print("현재 학생번호 :", stuNo)
  print(students)