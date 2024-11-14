import random

# 1-25까지 랜덤의 숫자 25개를 중복없이 추출해서
# [5, 5] 2차원 리스트에 입력해서 출력하시오.
a_list = []
for i in range(25):
  a_list.append(i + 1)

random.shuffle(a_list)
print(a_list)

b_list = []
for i in range(0, len(a_list), 5):
  b_list.append(a_list[i:i+5])

while True:
  print("\t0\t1\t2\t3\t4")
  print("-" * 60)
  for i in range(5):
    print(i, end="\t")
    for j in range(5):
      print(b_list[i][j], end="\t")
    print()
  point = input("좌표를 입력하세요.[0,1]>> ")
  p_list = point.split(",")
  print(f"{point} 좌표의 값 :", b_list[int(p_list[0])][int(p_list[1])])

# while len(a_list) < 25:
#   num = random.randint(1, 25)
#   if num not in a_list:
#     a_list.append(num)
# print(a_list)

# b_list = []
# for i in range(5):
#   a = []
#   for j in range(5):
#     a.append(a_list[5 * i + j])
#   b_list.append(a)
# print(b_list)