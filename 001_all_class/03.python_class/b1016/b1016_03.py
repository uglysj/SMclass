# students = [
#   {'no': 1, 'name': '홍길동', 'kor': 100, 'eng': 100, 'math': 99, 'total': 299, 'avg': 99.67, 'rank': 0},
#   [1, '홍길동', 100, 100, 99, 299, 99.66666666666667, 0],
#   [2, '유관순', 90, 90, 99, 279, 93.0, 0],
#   [3, '이순신', 80, 68, 49, 197, 65.66666666666667, 0]
# ]
stu_key = ['no', 'name', 'kor', 'eng', 'math', 'total', 'avg', 'rank']
students = []

# 파일읽기 - r
f = open('a.txt', 'r', encoding='UTF-8')
while True:
  line = f.readline()
  if not line: break
  s = line.strip().split(',')
  for i in range(len(s)):
    if i == 1: continue
    elif i == 6:
      s[i] = float(s[i])
    else:
      s[i] = int(s[i])
  students.append(dict(zip(stu_key, s)))
f.close()
print(students)