# 함수 - 기본매개변수, 가변매개변수, 키워드 매개변수

# 함수 - 가변매개변수, 키워드 매개변수 동시 사용할 경우
def plus(*n, k = 10): # 가변매개변수가 먼저, 다음 키워드 매개변수를 사용해야 함.
  print("k :", k)
  for i in n:
    print(i)

plus(1, 2, 3, 4 ,5, k = 50)

# print(1, 2, 3, 4, 5, sep="", end="\t")
# print(1)

# 3. 함수 - 키워드 매개변수
# def plus(k = 10, m = 5):
#   print("k :", k)
#   print("m :", m)

# plus(m = 1, k = 2) # 매개변수 개수가 일치하지 않으면 에러, 키워드 매개변수는 상관없음.

# 2. 함수 - 가변매개변수
# def plus(a, *n1): # 기본매개변수를 같이 사용하려면, 가변매개변수 앞에 사용
#   print("a :", a)
#   for i in n1:
#     print(i)
#   print(type(n1))

# plus(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

# 1. 함수 - 기본매개변수
# def plus(n1, n2):
#   sum = n1 + n2
#   print("합계 :", sum)

# 함수호출 - 매개변수 개수를 정확히 맞춰야 함. 맞추지 않으면 에러
# plus(10, 20)

# # 함수 선언
# def calc(start, end):
#   # 구구단
#   for i in range(start, end + 1):
#     print(f"[ {i} 단 ]")
#     for j in range(1, 10):
#       print(f"{i} * {j} = {i * j}")

# # -------------------------------
# # 2단 ~ 9단
# start = 2
# end = 9
# calc(start, end) # 함수 호출

# # 3단 ~ 7단
# start = 3
# end = 7
# calc(start, end) # 함수 호출

# # 5단 ~ 8단
# start = 5
# end = 8
# calc(start, end) # 함수 호출