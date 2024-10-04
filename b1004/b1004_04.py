### 변수 치환 방법 사용 ###
# a = int(input("숫자 입력 : "))
# b = int(input("숫자 입력 : "))
# sum = 0

# if a > b:
#   a, b = b, a # 파이썬만 가능 - 두개 변수 치환
# for i in range(a, b + 1):
#   sum += i
# print(f"합계 : {sum}")

### min, max 함수 사용 ###
# a = int(input("숫자 입력 : "))
# b = int(input("숫자 입력 : "))
# sum = 0

# for i in range(min(a, b), max(a, b) + 1):
#   sum += i
# print(f"합계 : {sum}")

### if문 사용 ###
# a = int(input("숫자 입력 : "))
# b = int(input("숫자 입력 : "))
# sum = 0

# min_num, max_num = a, b
# if a > b:
#   min_num = b; max_num = a
# for i in range(min_num, max_num + 1):
#   sum += i
# print(f"합계 : {sum}")

# if a < b:
#   for i in range(a, b + 1):
#     sum += i
# else:
#   for i in range(b, a + 1):
#     sum += i
# print(f"합계 : {sum}")
  
# sum = 0
# for i in range(1, 100 + 1, 2):
#   sum += i
# print(f"합계 : {sum}")

# sum = 0
# for i in range(1, 100 + 1):
#   sum += i
# print(f"합계 : {sum}")

# for i in range(3):
#   print(f"{i}: 안녕하세요.")

# for _ in range(3):
#   print("안녕하세요.")

# for i in [1, 2, 3]:
#   for j in range(i):
#     print("안녕하세요.")
#   print("-" * 20)

# for i in [1, 2, 3]:
#   print("안녕하세요.\n" * i, end = "")
#   print("-" * 20)

# for i in range(5, 0, -1): # -1씩 감소
#   print("*" * i)

# for i in range(5):
#   print("*" * (i + 1))

# for문을 사용해서 "*" 찍기
# for i in range(5):
#   for j in range(5):
#     print("*")

# range(시작값, 끝값 + 1, 증가값)
# for i in range(1, 10, 2):
#   for j in range(1, 10):
#     print(f"{i} x {j} = {i * j}")
#   print("-" * 20)

# 구구단 1, 3, 5, 7, 9단 출력하시오.
# for i in range(1, 10, 1):
#   if i % 2 != 0:
#     for j in range(1, 10):
#       print(f"{i} x {j} = {i * j}")
#     print("-" * 20)     
   
# # 구구단을 출력하시오.
# for i in range(2, 10):
#   print(f"[ {i} 단 ]")
#   for j in range(1, 10):
#     print(f"{i} x {j} = {i * j}")
#   print("-" * 20)

# 1, 3, 5, 7, 9 까지 출력하시오.
# for i in range(1, 10 + 1):
#   if i % 2 != 0:
#     print(i)

# 1, 10까지 for문을 사용해서 출력하시오.
# for i in range(1, 10 + 1):
#   print(i)