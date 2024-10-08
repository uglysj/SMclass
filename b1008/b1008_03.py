import random
# 25개 1차원 리스트 -> 1, 25 입력한 후 랜덤으로 다시 출력하시오.
# [5,5] 2차원 리스트 입력 후 출력하시오.
aArr = []
for i in range(25):
  aArr.append(i + 1)
random.shuffle(aArr)

# while len(aArr) < 25:
#   num = random.randint(1, 25)
#   if num not in aArr:
#     aArr.append(num)

a_list = []
for i in range(5):
  a = []
  for j in range(5):
    a.append(aArr[i * 5 + j])
  a_list.append(a)

while True:
  print("\t0\t1\t2\t3\t4")
  print("-" * 50)
  for i in range(5):
    print(i, " |", end="\t")
    for j in range(5):
      print(a_list[i][j], end="\t")
    print()
  
  num = int(input("값을 입력하세요 >> "))
  if 1 <= num <= 25:
    for i in range(5):
      for j in range(5):
        if num == a_list[i][j]:
          print(f"위치 값 : {i, j}")
          a_list[i][j] = 'x'
  else:
    print("잘못된 값 입력")
    continue
      
  # code = input("좌표를 입력하세요(ex. 0.0) >> ")
  # cList = code.split(".")
  # print(f"{cList} 좌표 값 :", a_list[int(cList[0])][int(cList[1])])