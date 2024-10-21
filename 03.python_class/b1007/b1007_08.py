import random

lotto = [0] * 6 + [1] * 3
random.shuffle(lotto)

a_list = []
for i in range(3):
  a = []
  for j in range(3):
    a.append(lotto[i * 3 + j])
  a_list.append(a)

aa_list = [
  ["로또"] * 3,
  ["로또"] * 3,
  ["로또"] * 3
]

while True:
  print("\t0\t1\t2")
  print("-" * 30)
  for i in range(3):
    print(i, "|", end="\t")
    for j in range(3):
      print(aa_list[i][j], end="\t")
    print()
  code = input("좌표 입력(ex. 0,1) >> ")
  cList = code.split(",")
  if a_list[int(cList[0])][int(cList[1])] == 1:
    aa_list[int(cList[0])][int(cList[1])] = '당첨'
    print("당첨되었습니다.")
  else:
    aa_list[int(cList[0])][int(cList[1])] = '꽝'
    print("꽝입니다.")