# if - else
# if - elif - else

score = int(input("입력 : "))
if score >= 90:
  if score >= 98:
    print("A+")
  elif score >= 94:
    print("A")
  else:
    print("A-")
elif score >= 80:
  if score >= 88:
    print("B+")
  elif score >= 84:
    print("B")
  else:
    print("B-")
elif score >= 70:
  if score >= 78:
    print("C+")
  elif score >= 74:
    print("C")
  else:
    print("C-")
elif score >= 60:
  if score >= 68:
    print("D+")
  elif score >= 64:
    print("D")
  else:
    print("D-")
else:
  print("F")

# month = int(input("입력 : "))
# if month >= 3 and month <= 5:
#   print("봄")
# elif month >= 6 and month <= 8:
#   print("여름")
# elif month >= 9 and month <= 11:
#   print("가을")
# elif month >= 1 and month <= 2 or month == 12:
#   print("겨울")
# else:
#   print("잘못된 월 입력")

# num = int(input("입력 : "))
# if num <= 10 or num >= 100:
#   print("정답")
# else:
#   print("오답")

# num = int(input("입력 : "))
# if num >= 1 and num <= 10:
#   print("정답")
# else:
#   print("오답")

# if 1 <= num <= 10:
#   print("정답")
# else:
#   print("오답")


# num = int(input("입력 : "))
# if num % 2 == 0:
#   print("짝수")
# else:
#   print("홀수")