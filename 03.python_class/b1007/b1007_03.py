a_list = []
for i in range(5):
  a = []
  for j in range(5):
    a.append(5 * i + (j + 1))
  a_list.append(a)
print(a_list)

# a_list = [] # a_list[0], a_list[1], ...
# for i in range(9):
#   a_list.append(i + 1)

# b_list = []
# for i in range(9):
#   pass  
# print(b_list)

# a_list = []
# for i in range(3):
#   a = []
#   for j in range(3):
#     a.append(3 * i + (j + 1))
#   a_list.append(a)
# print(a_list)

# b_list = []
# for i in range(1, 10):
#   b_list.append(i)
# print(b_list)

# 2차원 리스트
# a_list = [
#   [1, 2, 3, 4],
#   [5, 6, 7, 8],
#   [9, 10, 11, 12]
# ]

# 2차원리스트 -> for문을 2번 사용
# for i in a_list:
#   for j in i:
#     print(j)