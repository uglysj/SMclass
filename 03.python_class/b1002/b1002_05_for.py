students = [
  [1, "홍길동", 100, 90, 99],
  [2, "유관순", 100, 100, 99],
  [3, "이순신", 100, 100, 99]
]
# print(len(students))

# 반복문
for i in range(10): # 시작 0부터 10번 반복 (0 - 9)
  print("{}".format(i), end=" ")

print("\n")
for i in range(2, 5): # 시작 2부터 5 이전까지 반복 (2 - 4)
  print("{}".format(i), end=" ")

print("\n")
for i in range(1, 10, 2): # 시작 1부터 10 이전까지 2씩 건너뛰며 출력 (1 3 5 7 9)
  print("{}".format(i), end=" ")

print("\n")
aArr = [1, 2, 5, 7, 8]
for i in aArr: # list의 값을 1개씩 가져와서 출력 (1 2 5 7 8)
  print("{}".format(i), end=" ")

print("\n")
for i, data in enumerate(aArr): #list의 값과 index번호를 함께 출력
  print(i, ":", data)

aStr = "안녕하세요"
for i in aStr: # 문자열의 값을 1개씩 가져와서 출력
  print("{}".format(i), end="")

print("\n")
for idx, data in enumerate(aStr): #enumerate는 index번호를 추가해서 가져올 수 있음.
  print(idx, ":", data)

# 번호, 이름, 국어, 영어, 수학
# s = [4, "강감찬", 100, 90, 99]
# print(s)
# s.append(s[2] + s[3] + s[4])
# print(s)
# s.append(s[5] / 3)
# print(s)

# list 추가 - append: 뒤에추가, insert: 원하는 위치추가
# 삭제 - del: 위치삭제, remove: 값으로 검색해서 삭제
# a_list = [1, 2 ,3]
# a_list.append(10) # 마지막에 10추가
# print(a_list)

# a_list.insert(2, 100) # 2번째 자리에 100추가
# print(a_list)

# del a_list[1] # 1번째 자리 삭제
# print(a_list)

# a_list.remove(100) # 해당 값으로 삭제
# print(a_list)

# 문자열 슬라이싱
# str = "좋은 하루되세요. 많은 행복받으세요. 많은 감사! 많은 돈"
# print(len(str))

# # 뒤쪽에서 5자리 전까지 출력
# print(str[-5:])
# print(str[-1])