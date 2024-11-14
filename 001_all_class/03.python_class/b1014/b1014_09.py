a = 10 # 전역변수
def calc(a):
  a += 10
  print(a)
calc(a)

# 함수 - 매개변수 (일반변수, 복합변수)
# 3. 함수 복합매개변수 - return 없이 값이 함수 밖으로 값 사용 가능
# def calc(hArr):
#   for i in range(len(hArr)):
#     hArr[i] += 100

# hArr = [1, 2, 3, 4, 5] # 복합변수 - 주소 값이 저장됨.
# calc(hArr)
# print(hArr)

# 2. 전역변수 - 일반매개변수 return 없이 함수 밖으로 값 사용 가능
# def calc():
#   global h
#   h += 100

# h = 20
# calc() # 함수호출 후 h에 값을 할당할 필요 없음.
# print(h)

# 1. 함수 일반매개변수 - return이 아니면 값이 함수 밖으로 나올 수 없음.
# def calc(h):
#   h += 100
#   return h

# h = 20
# h = calc(h) # 함수호출만 하고 변수에 값을 넣어주지 않으면 값이 변경되지 않음.
# print(h)