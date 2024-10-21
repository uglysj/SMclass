fruit = []

while True:
  # strip() 앞, 뒤쪽 여백 제거 trim
  # replace(" ", "") = 문자 대체 함수
  search = input("과일 이름 입력(종료 : x) : ").replace(" ", "")
  # search = input("과일 이름 입력(종료 : x) : ").strip()
  if search == 'x':
    break
  if search in fruit:
    print("중복된 과일 이름 입력 함.")
  else:
    print(f"{search}를(을) 추가합니다.")
    fruit.append(search)
    print("모든 과일이름 : ", fruit)

# 반복문을 종료할 때 = break
# while True:
#   break
# print("프로그램 종료")

# 무한 반복문은 while True 입력
# a = 0
# while True: # 무한 반복
#   print(a)
#   a += 1

# while a < 10:
#   a += 1
#   print(a)
# print("프로그램 종료")