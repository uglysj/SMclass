import sys
list = []
for i in range(9):
  list.append(int(sys.stdin.readline()))
print(max(list))
print(list.index(max(list)) + 1)