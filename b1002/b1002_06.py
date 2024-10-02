students = [
  [1, "홍길동", 100, 90, 99],
  [2, "유관순", 100, 100, 99],
  [3, "이순신", 100, 100, 99]
]
ss = [4, "강감찬", 100, 90, 99]

students.append(ss)
print(students)

for idx, s in enumerate(students):
  if s[1] == "이순신":
    del students[idx]
print(students)

# for s in students:
#   if s[1] == "이순신":
#     students.remove(s)
# print(students)

# print(students) # 한번에 모두 출력

# for s in students: # 1개씩 가져와서 출력
#   print(s)

# for s in students:
#   if s[1] == "유관순":
#     print(s)