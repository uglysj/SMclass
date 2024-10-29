title = ['e_id', 'e_name', 'salary']
a = [
  (196, 'Alana Walsh', 3100.0),
  (125, 'Julia Nayer', 3200.0),
  (180, 'Winston Taylor', 3200.0),
  (194, 'Samuel McCain', 3200.0),
  (138, 'Stephen Stiles', 3200.0)
]
aa = []

for i in a:
  aa.append(dict(zip(title, i)))
print(aa)

# print(type(a))
# print(dict(zip(title, a)))

# name = '홍길동'
# # 문자변수 출력
# print('안녕하세요. 이름은 %s' % name)
# # format 함수
# print('Hello. my name is {}'.format(name))
# # 문자 f 함수
# print(f'Hello. my name is {name}')

# a = 1
# b = 2

# a_list = [a, b]
# print(type(a_list))
# b_list = [b]
# print(type(b_list))

# 튜플을 1개만 지정할 때는 뒤에 ,를 넣어야 함.
# a_tuple = (a, b)
# print(type(a_tuple))
# b_tuple = (a,)
# print(type(b_tuple))