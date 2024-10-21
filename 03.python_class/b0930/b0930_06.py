stu_data = ["홍길동", 100, 100, 100, 99]
# for s in stu_data:
#   print(s)
stu_title = ["번호", "이름", "국어", "영어", "수학", "과학", "합계", "평균"]
stu_datas = [[1, "유관순", 100, 100, 100, 99], [2, "이순신", 100, 99, 98, 99], [3, "김구", 80, 100, 90, 99]]

# print("{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}".format(stu_title[0], stu_title[1], stu_title[2], stu_title[3], stu_title[4], stu_title[5], stu_title[6], stu_title[7]))
# print("-" * 60)
print("\t\t   [ 학생성적 프로그램 ] ")
for s_t in stu_title:
  print("{}".format(s_t),end='\t')
print()
print("-" * 61)

for s in stu_datas:
  print("{}\t{}\t{}\t{}\t{}\t{}\t{}\t{:.2f}".format(s[0], s[1], s[2], s[3], s[4], s[5], s[2] + s[3] + s[4] + s[5], (s[2] + s[3] + s[4] + s[5]) / 4))
## 번호, 이름, 국어, 영어, 수학, 과학, 합계, 평균

# total = stu_datas[1][1] + stu_datas[1][2] + stu_datas[1][3] + stu_datas[1][4]
# avg = total / 4
# print(f"이순신의 평균 : {avg}")

# print(f"학생이름 : {stu_data[0]} \n국어 : {stu_data[1]} \n영어 : {stu_data[2]} \n수학 : {stu_data[3]} \n과학 : {stu_data[4]} \n합계 : {total} \n평균 : {avg}")

# 2개의 길이를 입력받아, 삼각형의 넓이, 직사각형의 넓이를 구하시오
# length = input("2개의 길이를 입력 : ")
# l_list = length.split(" ")
# t_area = float(l_list[0]) * float(l_list[1]) / 2
# s_area = float(l_list[0]) * float(l_list[1])
# print(f"삼각형 넓이 : {t_area}")
# print(f"직사각형 넓이 : {s_area}")

# 원의 넓이 : 반지름 * 반지름 * 3.14
# radius = input("반지름 입력 : ")
# print((float(radius)**2) * 3.14)
# print("원의 넓이 : {:.2f}".format((float(radius)**2) * 3.14))

#### 복합대입연산자 +=, -=, *=, /=, //=, %=, **= ####
# a = 10
# a += 5; print(a)
# a -= 5; print(a)
# a *= 5; print(a)
# a /= 5; print(a)
# a //= 5; print(a)
# a %= 5; print(a)
# a **= 5; print(a)

#### 숫자형을 문자열로 변환 ####
# # 문자열 + 숫자 : 불가능
# a = 100
# b = 10
# print(str(a) + str(b))

#### 문자형 숫자 변환 ####
# a = "100"
# b = "10.5"
# c = "안녕"
# print(float(a)) # 정수형 문자열 -> 정수타입, 실수타입
# # print(int(b)) # 실수형 문자열 -> 실수타입
# print(float(c)) # 글자는 숫자형 타입으로 변경 불가

# aa = 10
# bb = 5
# # 1줄 선언 방식
# a = 10; b = 5
# c, d = 10, 20
# s1, s2, s3 = 1, 2, 3

#### 우선순위 계산 ####
# print(2 + 2 - 2 * 2 / 2 * 2)

#### 사칙연산(+ - * /) 추가적 연산(% // **) ####
# /, %, //, **
# a, b = 5, 3
# print("{} {} {} {}".format(a / b, a % b, a // b, a ** b))