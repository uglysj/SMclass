students = [
  [1, "홍길동", 100, 90, 99],
  [2, "유관순", 100, 100, 99],
  [3, "이순신", 100, 100, 99],
  [4, "강감찬", 100, 90, 99],
  [5, "김구", 90, 90, 99]
]

name = input("이름 입력 : ")
cnt = 0
for idx, s in enumerate(students):
  if s[1] == name:
    del students[idx]
    print(f"{name}을(를) 삭제합니다.")
    cnt = 1
    break
if cnt == 0:
  print("이름이 없습니다.")
else:
  print(students)

# all_list = [
#   [1, "홍길동", 100], [2, "유관순", 200], [3, "이순신", 100]
# ]
# a = [3, "이순신", 100]

# for s in all_list:
#   if s[1] == "유관순":
#     all_list.remove(s)
# print(all_list)

# all_list.remove(a)
# print(all_list)

# aArr = [2, 3, 4, 6, 7, 8, 9, 10]

# aArr.append(50); aArr.append(100)
# print(aArr)

# aArr.insert(2, 30)
# print(aArr)

# aArr.remove(6)
# print(aArr)

# del aArr[0]; del aArr[3]
# print(aArr)