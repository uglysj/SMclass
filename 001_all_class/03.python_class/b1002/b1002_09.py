fruit = "사과,배,딸기,포도,복숭아,배,사과,배,딸기"
fruits = fruit.split(",")
print(fruits)
print("전체개수 :", len(fruits))
search = input("과일 이름 입력 : ")
for idx, s in enumerate(fruits):
  if s == search:
    print("{}의 위치 : {}".format(search, idx))
print("{}의 개수 {}개".format(search, fruits.count(search)))

# print(fruit.find('배')) # 3
# print(fruit.find('배', fruit.find('배') + 1)) # 15
# print(fruit.find('배', fruit.find('배', fruit.find('배') + 1) + 1)) # 20

# print(fruit.find('딸기'))
# print(fruit.find('딸기', fruit.find('딸기') + 1))
# print(fruit.find('딸기', 6))
