stu_title = ["번호", "이름", "국어", "영어", "수학", "과학", "합계", "평균"]
stu_datas = [[1, "홍길동", 100, 100, 100, 99], [2, "유관순", 99, 99, 100, 99], [3, "이순신", 100, 99, 98, 99], [4, "김구", 80, 100, 90, 99], [5, "김유신", 80, 100, 90, 89]]

# stu_datas[0].append(100)
# print(stu_datas[0])

for s_t in stu_title:
  print("{}".format(s_t), end = '\t')
print()
print("-" * 61)

for s_d in stu_datas:
  s_d.append(s_d[2] + s_d[3] + s_d[4] + s_d[5])
  s_d.append((s_d[2] + s_d[3] + s_d[4] + s_d[5]) / 4)
  print("{}\t{}\t{}\t{}\t{}\t{}\t{}\t{:.2f}\t".format(s_d[0], s_d[1], s_d[2], s_d[3], s_d[4], s_d[5], s_d[6], s_d[7]))