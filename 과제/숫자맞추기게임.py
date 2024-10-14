import random

nList = [] # 입력한 숫자 저장용 리스트
rand = 0 # 랜덤 숫자 저장용 변수
num = 0 # 입력 숫자 저장용 변수
cnt = 0 # 실패확인용 변수

rand = random.randint(1, 100 + 1) # 랜덤숫자 발생
for i in range(10):
  num = int(input(f"{i+1}번째 도전! 숫자 입력(1~100) >> "))
  nList.append(num)

  if num > rand:
    print("입력한 숫자가 큽니다. 더 작게 입력하세요.\n")
  elif num < rand:
    print("입력한 숫자가 작습니다. 더 크게 입력하세요.\n")
  else:
    print(f"정답입니다. 정답은 : {rand}"); cnt = 1
    print(f"{i + 1}번째 도전동안 입력한 숫자 : {nList}")  
    break

# 실패했을 경우
if cnt == 0:
  print(f"10번 도전에 실패했습니다. 정답은 : {rand}")
  print(f"{i + 1}번째 도전동안 입력한 숫자 : {nList}")