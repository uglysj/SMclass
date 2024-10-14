# 두수를 입력받아 더하기를 출력하시오.
def plus(n1, n2):
  return n1 + n2

num1 = int(input("숫자1 입력 >> "))
num2 = int(input("숫자2 입력 >> "))
print(plus(num1, num2))

# def plus(n1, n2):
#   result = n1 + n2
#   return result

# print(plus(1, 2))
# print(plus(55, 45))
# print(plus(50, 50))

# # 2,50 합 3,7 합 5,50 합을 모두 더해서 출력하시오.
# def num_sum(start, end):
#   sum = 0
#   for i in range(start, end + 1):
#     sum += i
#   return sum

# print("2-50까지의 합 : {:,}".format(num_sum(2, 50)))
# print("3-7까지의 합 : {:,}".format(num_sum(3, 7)))
# print("5-50까지의 합 : {:,}".format(num_sum(5, 50)))
# total = num_sum(2, 50) + num_sum(3, 7) + num_sum(5, 50)
# print("합계 : {:,}".format(total))

# def num_sum(start, end):
#   sum = 0
#   for i in range(start, end + 1):
#     sum += i
#   return sum

# total = 0
# num_sum(1, 10)
# num_sum(1, 100)
# total = num_sum(1, 10) + num_sum(1, 100)

# # 1, 10까지의 합과 1, 100까지 합의 총합을 출력하시오.
# print("합계 :", total)
# print("프로그램 종료")

# def num_sum(start, end):
#   sum = 0
#   for i in range(start, end + 1):
#     sum += i
#   print("합계 :", sum)

# # 두수를 입력받아, 그 사이의 숫자 합을 구하시오.
# # num1, num2 변수이용, 함수를 사용해서 출력하시오.
# num1 = int(input("첫번째 번호 입력 >> "))
# num2 = int(input("두번째 번호 입력 >> "))
# num_sum(num1, num2)

# # 1-10까지 합계를 출력하시오.
# num_sum(1, 10)

# # 1-100까지 합계를 출력하시오.
# num_sum(1, 100)

# # 2-50까지 합계를 출력하시오.
# num_sum(2, 50)

# # 100-1000까지 합계를 출력하시오.
# num_sum(100, 1000)