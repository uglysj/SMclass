class Student:
  # 인스턴스 변수 - 객체선언을 하면 변수는 개별적으로 생성
  count = 0 # 클래스 변수 - 모든 객체가 동일한 변수를 사용
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

  # == : 호출되는 함수
  def __eq__(self, value): # self: 현재자신 객체, value : 비교할 다른 객체
    return self.total == value.total
  def __ne__(self, value): # self: 현재자신 객체, value : 비교할 다른 객체
    return self.total != value.total
  def __gt__(self, value): # self: 현재자신 객체, value : 비교할 다른 객체
    return self.total > value.total
  def __ge__(self, value): # self: 현재자신 객체, value : 비교할 다른 객체
    return self.total >= value.total
  def __lt__(self, value): # self: 현재자신 객체, value : 비교할 다른 객체
    return self.total < value.total
  def __le__(self, value): # self: 현재자신 객체, value : 비교할 다른 객체
    return self.total <= value.total

s1 = Student('홍길동', 100, 100, 100) # 300
s2 = Student('유관순', 100, 100, 100) # 290

if 300 > 290: 
  print("숫자 비교 : 참")
else: 
  print("숫자 비교 : 거짓")

if s1 != s2: # 항목 중에 어떤 것으로 비교
  print("객체 비교 : 참")
else: 
  print("객체 비교 : 거짓")