def calc(num, num2, op):
  if op == '+':
    return num + num2
  elif op == '-':
    return num - num2
  elif op == '*':
    return num * num2
  elif op == '/':
    return num / num2

num = int(input("숫자를 입력하세요. >> "))
num2 = int(input("숫자를 입력하세요. >> "))
op = input("+, -, *, / 중 하나를 선택하세요. >> ")

print("결과 값 :", calc(num, num2, op))