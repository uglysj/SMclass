import random

# 1-100까지의 랜덤숫자를 생성
# 입력한 숫자가 랜덤숫자보다 크면 입력한 숫자가 큽니다.
# 입력한 숫자가 랜덤숫자보다 작으면 입력한 숫자가 작습니다.
# 10번 도전하도록 하시오.
# 정답입니다. 프로그램종료 하시오. break

r_num = random.randint(1, 100)
cnt = 0

### while문 ###
# i = 0
# while i < 10:
#   num = int(input("숫자 입력(1-100) : "))
#   if num == r_num:
#     print("정답입니다. 정답번호 : {}".format(r_num))
#     cnt = 1
#     break
#   elif num > r_num:
#     print("랜덤숫자보다 큽니다.")
#   else:
#     print("랜덤숫자보다 작습니다.")
#   i += 1
# if cnt == 0:
#   print("10번 도전 실패 프로그램 종료. 정답번호 : {}".format(r_num))

### for문 ###
for i in range(10):
  num = int(input("숫자 입력(1-100) : "))
  if num == r_num:
    print("정답입니다. 정답번호 : {}".format(r_num))
    cnt = 1
    break
  elif num > r_num:
    print("랜덤 숫자보다 큽니다.")
  else:
    print("랜덤 숫자보다 작습니다.")
if cnt == 0:
  print("10번 도전 실패 프로그램 종료. 정답번호 : {}".format(r_num))