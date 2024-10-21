students = []
subject = ['번호', '이름', '국어', '영어', '수학', '합계', '평균', '등수']
sub = ['no', 'name', 'kor', 'eng', 'math', 'total', 'avg', 'rank']
f = open('b1017/students.txt', 'r', encoding='UTF8')
while True:
  line = f.readline().strip()
  if not line: break
  s = line.split(',')
  for i in range(len(s)):
    if i == 1: continue
    elif i == 6: s[i] = float(s[i])
    else: s[i] = int(s[i])
  students.append(dict(zip(sub, s)))
f.close()