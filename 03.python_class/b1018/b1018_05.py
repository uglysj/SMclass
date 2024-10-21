class Circle:
  def __init__(self, radius):
    self.__radius = radius

  # 원의 넓이
  def get_area(self):
    return self.__radius ** 2 * 3.14

  # 원의 둘레
  def get_circum(self):
    return self.__radius * 2 * 3.14  

  def get_radius(self):
    return self.__radius
  
  def set_radius(self, radius):
    self.__radius = radius

  def __str__(self):
    c_str = '원의 반지름 : {}, 원의 넓이 : {}, 원의 둘레 : {}'.format(self.__radius, self.get_area(), self.get_circum())
    return c_str
  
c1 = Circle(10)
print(c1)

# 클래스 선언
# c1 = Circle(10)
# print('c1 반지름 :', c1.get_radius())
# c1.set_radius(200)
# print('c1 반지름 변경 :', c1.get_radius())
# c1.__radius = 100
# print("직접 변경 :", c1.__radius)
# print('get 읽어온 radius :', c1.get_radius())
# print(dir(c1))