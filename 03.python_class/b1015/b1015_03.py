# 기본매개변수로 값 전달 - return 필요, 값 전달 필요
def plus(a):
  a += 10
  print("지역변수 a :", a)
  return a

a = 10 # 전역변수
a = plus(a) # a 변수에 값을 전달해야만 변경이 됨.
print("전역변수 a :", a)

# 복합매개변수로 값 전달 - 리스트, 딕셔너리 / return 필요 없음.
# def plus(a):
#   a[0] = 100
#   a[1] = 200
#   print("지역변수 a :", a)

# a = [10, 20] # 전역변수
# plus(a)
# print("전역변수 a :", a)