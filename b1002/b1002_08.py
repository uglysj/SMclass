# 리스트
# in = 데이터가 있는지 확인
# count = 데이터의 개수
# find = 데이터가 있는 위치, 없으면 -1 find(검색어, 시작위치, 끝위치)
# index = 데이터가 있는 위치, 없으면 에러

fruit = "사과,배,딸기,포도,복숭아,배,사과,배,딸기"
search = input("과일 이름 입력 : ")
print("모든 글자 :", fruit)
idx = 0
if fruit.count(search) > 0:
  for i in range(fruit.count(search)):
    print(f"{search} 글자가 있는 위치 : ", fruit.find(search, idx)) # find(찾을문자, 시작 index, 끝 index)
    idx = fruit.find(search, idx) + 1
else:
  print(f"{search}(이)라는 글자는 없습니다.")

print(fruit[22])


# # count = 문자열 내에 해당 숫자 개수 확인
# fruit = "사과,배,딸기,포도,복숭아,배,사과,배,딸기"
# search = input("과일 입력 : ")
# if search in fruit:
#   print(f"{search}는(은) 있습니다.")
#   print("과일검색개수 : {}".format(fruit.count(search)))
#   print(fruit.find(search))
#   # print(fruit.index(search)) # search가 있는 위치의 index
# else:
#   print(f"{search}는(은) 없습니다.")
#   print(fruit.find(search))
#   # print(fruit.index(search)) # search가 있는 위치의 index
# print(fruit.count('사과'))

# count = 리스트에서 개수 확인
# fruit = ['사과', '배', '딸기', '포도', '복숭아', '배', '사과', '배', '딸기']
# print(fruit.count('배'))
# print(fruit.count('사과'))

# fruit = ['사과', '배', '딸기', '포도', '복숭아']
# s = input("과일 입력 : ")
# if s in fruit:
#   print(f"{s}는(은) 있습니다.")
# else:
#   print(f"{s}는(은) 없습니다.")

# fruit = "사과, 배, 딸기, 포도"
# if '배' in fruit:
#   print("배가 있습니다.")
# else:
#   print("배가 없습니다.")

# fruit = ['사과', '배', '딸기', '포도', '배']
# if '배' in fruit: # 1번의 비교로 있는지 확인
#   print("배가 있습니다.")
# else:
#   print("배가 없습니다.")