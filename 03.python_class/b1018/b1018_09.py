# Student 클래스 생성 후
# 데이터를 직접 입력을 받아, 클래스 선언 후 저장
# 번호 - 자동부여, 이름, 국어, 영어, 수학, 합계, 평균, 등수
# 클래스 전체 출력
# 클래스 수정

# [ 학생성적 프로그램 ]
# 1. 학생성적입력
# 2. 학생성적출력
# 3. 학생성적수정

class Student:
  stuNo = 0
  students = []
  s_title = ['번호', '이름', '국어', '영어', '수학', '합계', '평균', '등수']

  def __init__(self, name, kor, eng, math):
    Student.stuNo += 1
    self.no = Student.stuNo
    self.name = name
    self.kor = kor
    self.eng = eng
    self.math = math
    self.total = kor + eng + math
    self.avg = self.total / 3
    self.rank = 0
    Student.students.append(self)
  
  # def __str__(self):
  #   return f"{self.no}\t{self.name}\t{self.kor}\t{self.eng}\t{self.math}\t{self.total}\t{self.avg:.2f}\t{self.rank}"

  @classmethod
  def stu_output(self):
    print(*self.s_title, sep='\t'); print("-" * 65)
    for s in self.students:
      print(s)

  def stu_update(self):
    pass  


while True:
  print("[ 학생성적 프로그램 ]")
  print("1. 학생성적입력")
  print("2. 학생성적출력")
  print("3. 학생성적수정")
  choice = int(input("원하는 번호를 입력하세요.>> "))

  if choice == 1:
    print("[ 학생성적 입력 ]")
    name = input("이름을 입력하세요.>> ")
    score = []
    for i in range(3):
      score.append(int(input(f"{Student.s_title[i + 2]}점수를 입력하세요.>> ")))
    Student(name, *score)
  elif choice == 2:
    print("[ 학생성적 출력 ]")
    Student.stu_output()
  elif choice == 3:
    print("[ 학생성적 수정 ]")
    chk = 0
    name = input("이름을 입력하세요.>> ")
    for s in Student.students:
      if name == s.name:
        chk = 1
        print("[ 수정과목 선택 ]"); print("-" * 30)
        print("1. 국어점수")
        print("2. 영어점수")
        print("3. 수학점수"); print("-" * 30)
        choice = int(input("원하는 번호를 입력하세요.>> "))

        if choice == 1:
          print(f"현재 {Student.s_title[choice + 1]}점수 : {s.kor}")
          s.kor = int(input("수정점수 입력 >> "))
          print(f"수정 {Student.s_title[choice + 1]}점수 : {s.kor}\n")
        elif choice == 2:
          print(f"현재 {Student.s_title[choice + 1]}점수 : {s.eng}")
          s.eng = int(input("수정점수 입력 >> "))
          print(f"수정 {Student.s_title[choice + 1]}점수 : {s.eng}\n")
        elif choice == 3:
          print(f"현재 {Student.s_title[choice + 1]}점수 : {s.math}")
          s.math = int(input("수정점수 입력 >> "))
          print(f"수정 {Student.s_title[choice + 1]}점수 : {s.math}\n")

        s.total = s.kor + s.eng + s.math
        s.avg = s.total / 3
    
    if chk == 0:
      print("찾으려는 학생이 없습니다.\n")