class Student:
  # 인스턴스 변수 - 객체선언을 하면 변수는 개별적으로 생성
  count = 0 # 클래스 변수 - 모든 객체가 동일한 변수를 사용
  students = [] # 클래스 리스트
  s_title = ['번호', '이름', '국어', '영어', '수학', '합계', '평균', '등수']

  # 클래스 함수 선언
  @classmethod
  def stu_print(cls):
    print(*cls.s_title, sep='\t'); print("-" * 65)
    for s in cls.students:
      print(str(s))

  def __init__(self, name, kor, eng, math):
    Student.count += 1
    self.no = Student.count
    self.name = name
    self.kor = kor
    self.eng = eng
    self.math = math
    self.total = kor + eng + math
    self.avg = self.total / 3
    self.rank = 0
    # 클래스 리스트에 추가
    Student.students.append(self)

  # 객체를 문자열리턴 함수 - 리턴 : 항상 문자열이 되어야 함.
  def __str__(self):
    return f"{self.no}\t{self.name}\t{self.kor}\t{self.eng}\t{self.math}\t{self.total}\t{self.avg:.2f}\t{self.rank}"

  def print(self): # 딕셔너리 타입으로 리턴
    return {'no': self.no, 'name': self.name, 'kor': self.kor, 'eng': self.eng, 'math': self.math, 'total': self.total, 'avg': self.avg, 'rank': self.rank}

##### 프로그램 시작 #####
s_keys = ['no', 'name', 'kor', 'eng', 'math', 'total', 'avg', 'rank']

while True:
  print("[ 학생성적 프로그램 ]")
  print("1. 학생성적입력")
  print("2. 학생성적출력")
  print("3. 홍길동, 유관순 비교")
  choice = int(input("원하는 번호를 입력하세요.>> "))

  if choice == 1:
    print("[ 학생성적 입력 ]")
    name = input("이름을 입력하세요.>> ")
    score = []
    for i in range(3):
      score.append(int(input(f"{Student.s_title[i + 2]}점수를 입력하세요.>> ")))
    Student(name, *score)
    
    # 클래스 변수 접근 방법
    for s in Student.students:
      print(s)

    # 인스턴스변수 참조변수.변수명, 참조변수.함수명
    # 클래스변수 클래스명.변수명, 클래스명.함수명
  elif choice == 2:
    print("[ 학생성적 출력 ]") 
    Student.stu_print() # 클래스 함수 호출
  elif choice == 3: # 홍길동 학생합계, 유관순 학생합계
    s1 = Student('홍길동', 100, 100, 90)
    s2 = Student('유관순', 90, 100, 90)


# print(s1) # 주소 값 -> __str__() 정의 된 형태로 출력
# print(s1.print())
# students.append(s1.print())
# s2 = Student('유관순', 99, 99, 98)
# print(s2.print())
# students.append(s2.print())
# print(students)

# s1 = Student('홍길동', 100, 100, 99)
# print(s1.name)
# print('s1.count :', s1.count)
# s2 = Student('유관순', 90, 90, 50)
# print(s2.name)
# print('s2.count :', s2.count)
# print('s1.count :', s1.count)