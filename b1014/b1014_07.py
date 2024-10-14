stu_title = ['국어', '영어', '수학']
students = {'국어': 100, '영어': 100, '수학': 99, '합계': 299}

def s_modifiy(choice):
  print("현재 {}점수 : {}".format(stu_title[choice - 1], students[stu_title[choice - 1]]))
  students[stu_title[choice - 1]] = int(input(f"수정할 {stu_title[choice - 1]} 점수를 입력하세요.>> "))

print("[ 점수 수정 ]")
print("1. 국어점수")
print("2. 영어점수")
print("3. 수학점수")
choice = int(input("수정하려는 과목을 선택하세요.>> "))
if choice == 1:
  s_modifiy(choice)
elif choice == 2:
  s_modifiy(choice)
elif choice == 3:
  s_modifiy(choice)

students['합계'] = students['국어'] + students['영어'] + students['수학']
print("변경 :", students)