stu_title = ["번호", "이름", "국어", "영어", "수학", "과학", "합계", "평균"]
stu_datas = [[1, "홍길동", 100, 100, 100, 99], [2, "유관순", 99, 99, 100, 99], [3, "이순신", 100, 99, 98, 99], [4, "김구", 80, 100, 90, 99], [5, "김유신", 80, 100, 90, 99]]

for s_title in stu_title:
  print("{}".format(s_title), end = '\t')

print()
print("-" * 61)

for s_data in stu_datas:
  print("{}\t{}\t{}\t{}\t{}\t{}\t{}\t{:.2f}".format(s_data[0], s_data[1], s_data[2], s_data[3], s_data[4], s_data[5], s_data[2] + s_data[3] + s_data[4] + s_data[5], (s_data[2] + s_data[3] + s_data[4] + s_data[5]) / 4))