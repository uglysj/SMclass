for k in range(2, 10):
  print(f"[ {k} 단 ]", end = "\t")
print()
for i in range(1, 10):
  for j in range(2, 10):
    print(f"{j} x {i} = {j * i}", end="\t")
  print()

# for i in range(1000):
#   print("{:03d}".format(i))

# for i in range(10):
#   for j in range(10):
#     for k in range(10):
#       print(f"{i}{j}{k}")

# 구구단 입력한 단까지 출력하시오.
# num = int(input("숫자 입력 : "))
# for i in range(1, num + 1):
#   for j in range(1, 10):
#     print(f"{i} x {j} = {i * j}")
#   print("-" * 20)

# # 입력한 단만 출력
# for i in range(1, 10):
#   print(f"{num} x {i} = {num * i}")