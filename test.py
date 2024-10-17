import sys
N = int(input())
list = list(map(int, sys.stdin.readline().split(" ")))
s_num = int(input())
print(list.count(s_num))