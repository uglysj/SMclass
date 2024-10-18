# 클래스 생성
class Circle:
  def __init__(self, radius):
    self.__radius = radius # 변수 직접적으로 접근 제한

  # 원의 넓이
  def get_area(self):
    return self.__radius ** 2 * 3.14

  # 원의 둘레
  def get_circum(self):
    return self.__radius * 2 * 3.14

# 클래스 선언
c1 = Circle(int(input("반지름을 입력하세요.>> ")))

c1.radius = 7
print("원의 둘레 :", c1.get_circum())
print("원의 넓이 :", c1.get_area())

c2 = Circle(int(input("반지름을 입력하세요.>> ")))
print("원의 둘레 :", c2.get_circum())
print("원의 넓이 :", c2.get_area())
# print(c1.radius)

# # 절차적인 형태의 프로그램 구현
# # 반지름을 입력받아, 원의 둘레와 넓이를 출력하시오.

# radius = int(input("반지름 입력 >> "))
# print("원의 둘레 :", radius * 2 * 3.14)
# print("원의 넓이 :", radius ** 2 * 3.14)