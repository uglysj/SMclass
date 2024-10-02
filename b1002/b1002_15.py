# 숫자 맞추기
import random

rand = random.randint(1, 100)
cnt = 0

# i = 0
# while i < 10:
#   num = int(input(f"{i + 1}회 도전 숫자 입력(1-100) : "))
#   if num == rand:
#     print(f"정답입니다. {i + 1}회 만에 성공! 정답은 : {rand}")
#     cnt = 1
#     break
#   elif num > rand:
#     print("입력한 숫자가 큽니다.")
#   else:
#     print("입력한 숫자가 작습니다.")
#   i += 1
# if cnt == 0:
#   print(f"10회 도전 실패입니다. 정답은 : {rand}")

for i in range(10):
  num = int(input(f"{i + 1}회 도전 숫자 입력(1-100) : "))
  if num == rand:
    print(f"정답입니다. {i + 1}회 만에 성공! 정답은 : {rand}")
    cnt = 1
    break
  elif num > rand:
    print("입력한 숫자가 큽니다.")
  else:
    print("입력한 숫자가 작습니다.")
if cnt == 0:
  print(f"10회 도전 실패입니다. 정답은 : {rand}")