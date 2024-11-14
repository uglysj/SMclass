import os

# f = open('b1017/cart.txt', 'r', encoding='UTF-8')
# while True:
#   line = f.readline().rstrip()
#   if not line: break
#   print(line)

if os.path.exists('b1017/cart.txt'):
  print("파일이 있습니다.")
else:
  print("파일이 없습니다.")