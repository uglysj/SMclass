subject = ['국어', '영어']
score = []

while True:
  print("1. 과목추가")
  print("0. 종료")
  choice = input("원하는 번호를 입력하세요.>> ")
  if choice == '1':
    s_input = input("과목을 추가하세요.>> ")
    subject.append(s_input)
  elif choice == '0': break

for i in range(len(subject)):
  score.append(int(input(f"{subject[i]}점수를 입력하세요.>> ")))

sum = 0
for i in range(len(subject)):
  print(f"{subject[i]} : {score[i]}")
  sum += score[i]
print("합계 :", sum)

# a = 10
# b = 20
# c = 30

# def add(b, c):
#   return b + c

# a += add(b, c)
# print("a + b + c의 합계 :", a)

# a = 10
# b = 20
# sum = 0

# def add(a, b):
#   return a + b

# sum = add(a, b)
# print("a + b의 합계 :", sum)

# a = 10 # 전역변수

# def func(a):
#   print("함수 내 a :", a)
#   a += 50
#   return a
#   # global a # 전역변수를 가져옴.
#   # a = 50

# a = func(a)
# print("함수 밖 a :", a)

# subject = ['국어', '영어']

# def output(subject):
#   print("과목"); print("-" * 20)
#   for s in subject:
#     print(s)

# while True:
#   print("[ 과목 생성 프로그램 ]")
#   s_input = input("원하는 과목을 입력하세요.>> ")
#   subject.append(s_input)
#   output(subject)