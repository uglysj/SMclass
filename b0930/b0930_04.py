# name, kor, eng, math, total, avg 출력
name = input("이름 입력 : ")
# 문자열에서 정수형으로 타입 변경 (input은 문자열로 받게됨)
kor = int(input("국어 점수 입력 : "))
eng = int(input("영어 점수 입력 : "))
math = int(input("수학 점수 입력 : "))
total = kor + eng + math
avg = total / 3
print("{} {} {} {} {} {:.2f}".format(name, kor, eng, math, total, avg))
print(f"{name} {kor} {eng} {math} {total} {avg:.2f}")

# a = '100'
# b = "200"
# print(type(a))
# print(type(b))
# print(a + b) # 문자 연결 연산자 100200
# print(int(a) + int(b)) # 타입변경
# name = "홍길동"
# # print(int(name)) # 문자를 숫자로는 변경이 불가능. 문자형 숫자는 가능
# c = "3.14"
# print(int(float(c))) # 실수형으로 변경 후 정수형으로 변경
# # print(int(c)) # 문자 실수형은 정수로 바로 변경은 불가
# print(str(c)) # 실수형을 문자열로 변경
# d = "True"
# print(bool(d)) # 문자불형은 불형으로 변경
# 타입 변경 - str, float, int, bool

# name = "홍길동"
# print(type(name))
# level = '3레벨'
# print(type(level))
# n = 3.14
# print(type(n))
# num = 100
# print(type(num))
# a_bool = True # True, False 대문자로 넣어야함.
# print(type(a_bool))

# var1 = 100
# var2 = var1
# var3 = var2
# var4 = var3
# print(var4)

# v4 = v3 = v2 = v1 = 10
# print(v4)