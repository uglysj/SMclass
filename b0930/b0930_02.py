print("%d은 %d의 배수입니다." % (10, 2))
a = 10
b = 2
print(a, b)

# 출력 자리수
print("%d" % b)
print("%5d" % b) # 공간 5자리를 확보
print("%05d" % b) # 공간 확보 및 0으로 채움

num = 1
num2 = 10
num3 = 100
# print("%03d\n%03d\n%.2f" % (num, num2, num3))
# print("%5d\n" % (-10))

print("##### Quiz #####")
print("%.2f" % (758.12345678))
# 소수점도 1자리를 차지함.
print("%013.2f" % (25.05))

# 타입이 다른 것은 쉼표(,)로 구분
num4 = 150.15
print("정수 : %d" % (num4))
print("실수 : %f" % (num4))
print("문자열 : %s" % (num4))
print("*" * 10)

print("%5.1f" % (123456789.123))

# 10 * 2 = 20
# print("%d * %d = %d" % (a, b, a * b))

# 사용표시 - %s : 문자열, %c : 한글자, %f : 실수, %d : 정수
# 홍길동 총합 : 299, 평균 : 99.6666
# name = "홍길동"
# kor = 100
# eng = 100
# math = 99
# print("%s 총합 : %d, 평균 : %.2f" % (name, kor + eng + math, (kor + eng + math) / 3))

# 자리수 표시
# print()

#### print 사용 형태 ####
# print 쉼표, %, .format, f
# print(a,"은",b,"의 배수입니다.")
# print("%d은 %d의 배수입니다." % (a, b))
# print("{}은 {}의 배수입니다.".format(a, b)) 
# print(f"{a}은 {b}의 배수입니다.")