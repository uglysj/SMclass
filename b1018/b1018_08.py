# 변수 3종류
# 지역변수 : 함수내에 선언된 변수, 함수가 종료가 되면 사라짐.
# 인스턴스 변수 : 객체선언할 때 만들어짐, 각가의 객체마다 변수가 생성됨.
# - 참조변수명.변수명
# 클래스 변수 : 객체가 선언되지 않아도 만들어짐, 모든 객체가 공통으로 사용
# - 클래스명.변수명

# 함수 2종류
# 인스턴스 함수 : 객체선언할 때 만들어짐. 각각의 객체마다 함수가 생성됨.
# - 참조변수명.함수명
# 클래스 함수 : 객체가 선언되지 않아도 만들어짐, 모든 객체가 공통으로 사용
# - 클래스명.함수명
# @classmethod - 클래스함수표시

# 객체선언 한 참조변수를 출력하면 -> 주소 값이 출력됨.
# - 참조변수를 출력해서 원하는 데이터를 출력하려면 __str__ 를 사용해야 함.

class Student:
  stuNo = 1 # 클래스 변수
  students = []

  @classmethod
  def stu_print(cls):
    for s in cls.students:
      print(str(s))

  def __init__(self, name, kor, eng, math):
    self.no = Student.stuNo
    Student.stuNo += 1
    self.name = name
    self.kor = kor
    self.eng = eng
    self.math = math
    Student.students.append(self)
  #   self.total = kor + eng + math
  #   self.avg = self.total / 3
  #   self.rank = 0
  #   Student.student.append({'no': self.no, 'name': self.name, 'kor': self.kor, 'eng': self.eng, 'math': self.math, 'total': self.total, 'avg': self.avg, 'rank': self.rank})
  
  def __str__(self):
    return f"{self.no}, {self.name}, {self.kor}, {self.eng}, {self.math}" # 리턴 값 : 문자열 이어야 함.

  def get_no(self):
    return self.no

  def set_no(self, no):
    if no < 0: raise ValueError("0이하는 입력할 수 없습니다.")
    self.no = no

s1 = Student('홍길동', 100, 100, 100)
print(s1)
s2 = Student('유관순', 100, 100, 90)
print(s2)
s3 = Student('이순신', 100, 100, 80)
print(s3)
s4 = Student('강감찬', 100, 100, 70)
print(s4)
print("-" * 50)
# Student.stu_print()
for s in Student.students:
  print(s)

# s_title = ['번호', '이름', '국어', '영어', '수학', '합계', '평균', '등수']
# s_keys = ['no', 'name', 'kor', 'eng', 'math', 'total', 'avg', 'rank']
# # 1. 학생성적입력
# while True:
#   print("1. 학생성적입력")
#   choice = int(input("원하는 번호를 입력하세요.>> "))

#   if choice == 1:
#     print("[ 학생성적 입력 ]")
#     name = input("이름을 입력하세요.>> ")
#     score = []
#     for i in range(3):
#       score.append(int(input(f"{s_title[i + 2]}점수를 입력하세요.>> ")))
#     s1 = Student(name, *score)
#     for s in Student.student:
#       for i in s_keys:
#         if i == 'avg':
#           print(f"{s[i]:.2f}", end='\t')
#         else:
#           print(s[i], end='\t')
#       print()