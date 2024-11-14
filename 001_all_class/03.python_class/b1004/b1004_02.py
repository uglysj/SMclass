import random

# 랜덤숫자 : 1 ~ 100
rand = random.randint(1, 100)
# 성공 판별용 카운트
cnt = 0

for i in range(10):
  num = int(input(f"{i + 1}회 도전! 숫자 입력(1-100) : "))
  if num == rand:
    print(f"도전 {i + 1}회 만에 성공했습니다. 정답은 : {rand}")
    cnt = 1
    break
  elif num > rand:
    print("입력한 숫자가 큽니다. 더 작은 수를 입력하세요.")
  else:
    print("입력한 숫자가 작습니다. 더 큰 수를 입력하세요.")

if cnt == 0:
  print(f"10번 도전에 실패했습니다. 정답은 : {rand}")