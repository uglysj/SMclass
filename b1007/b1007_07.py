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
  ["로또", "로또", "로또"],
  ["로또", "로또", "로또"],
  ["로또", "로또", "로또"]
]

while True:
  my_money = int(input("얼마를 투자하시겠습니까? >> "))
  print("\t   [i, j 좌표]")
  print("\t0\t1\t2")
  print("-" * 28)
  for i in range(3):
    print(i, "|", end="\t")
    for j in range(3):
      print(aa_list[i][j], end="\t")
    print()

  code = input("좌표를 입력하세요(ex. 0.1) >> ")
  cList = code.split(".")
  if a_list[int(cList[0])][int(cList[1])] == 1:
    print(f"{cList} 당첨금 : {my_money * 10:,d}")
    aa_list[int(cList[0])][int(cList[1])] = "당첨"
  else:
    print(f"{cList} 다음기회에 : {my_money * 0}")
    aa_list[int(cList[0])][int(cList[1])] = "꽝"