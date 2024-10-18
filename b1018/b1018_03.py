# 클래스 생성
class Car:
  def __init__(self):
    self.color = '흰색'
    self.tire = 4
    self.gear = 'auto'
    self.__speed = 100

  def upSpeed(self, value):
    if value > 0: self.__speed += value
    else: raise Exception("값을 잘못 넣었습니다.")

  def downSpeed(self, value):
    self.__speed -= value

c1 = Car()
print(c1.color, c1.tire, c1.gear, c1.__speed)

# 클래스 사용하려면 클래스 선언!! 해야 함.
# c1 = Car('흰색', 4, 'auto', 100)
# print(c1.color)
# print(c1.tire)

# c2 = Car()
# c2.color = '빨강'
# print(c2.color)

# 리스트, 딕셔너리 변수 직접 값을 할당하는 방식

# speed 변수에 직접 값을 할당
# c1.speed = -100
# print(c1.speed)

# 함수를 활용해서 값을 할당
# c1.upSpeed(100)
# print(c1.speed)