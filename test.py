import sys
N, M = map(int, sys.stdin.readline().split(' '))
N_list = [i+1 for i in range(N)]
for a in range(M):
  i, j, k = map(int, sys.stdin.readline().split(' '))
  for b in range(i-1, j):
    N_list[b] = k

for i in range(len(N_list)):
  print(N_list[i], end=' ')