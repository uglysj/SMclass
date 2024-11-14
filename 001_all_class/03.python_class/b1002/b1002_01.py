# 문자열

# 문자열 숫자
a = "123"
print(type(a)) # str
print(type(int(a))) # int
print(type(float(a))) # float

b = "12.3"
# print(type(int(b))) # error - 소수점이 있는 문자열 숫자는 float만 변경가능함.
print(type(float(b))) # float

# 문자열 연결 연산자 +
s1 = "안녕"
s2 = "안녕하세요."
print(s1 + s2)
print(a + b) # 문자열 연결 연산자
# print(a * b) # error : 문자열에서 -,*,/ 은 안됨. 

# 문자열 * 2 / 문자열 반복 연산
print(s1 * 10)
print("-." * 30)

# 문자열 슬라이싱
str1 = "안녕하세요.반갑습니다." # 문자열 = 리스트 형태
print(str1[0])
print(str1[6])
print(str1[2:5]) # 해당범위출력 = [위치:숫자앞까지] = 하세요
print(str1[:5]) # [처음:숫자앞까지] = 안녕하세요
print(str1[2:]) # [위치:끝까지] = 하세요.반갑습니다.
print(str1[1:10:2]) # [위치:숫자앞까지:해당숫자씩] = 녕세.갑니
print(str1[1:10:3]) # [위치:숫자앞까지:해당숫자씩] = 녕요갑
print(str1[::-1]) # [처음:끝:역순] = .다니습갑반.요세하녕안

# [] - 배열 : 배열은 한번 범위가 정해지면 수정이 불가능 = c, 자바
# [] - 리스트 : 범위상관없음.

c = 12.3
print(type(int(c))) # 실수는 int 타입으로 변경 가능함.
print(int(c))

# input_str = input("글자를 입력하세요.\n")

# if input_str != "":
#   print("입력 문자 : " + input_str)
# else:
#   print("글자를 입력하셔야 합니다.")
# print("프로그램이 종료됩니다.")
