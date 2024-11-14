n_lists = ['10억', '9억 5,000', '11억 500', '7억', '12억 5,250']

a = '9억 5,000'
def num_chg(p):
  b = p.split('억')
  f_num = int(b[0]) * 100000000
  if b[1].strip() != '':
    s_num = int(b[1].strip().replace(',', '')) * 10000
  else:
    s_num = 0
  price = f_num + s_num
  return price

p_list = [num_chg(li) for li in n_lists]
print(p_list)

p_list2 = list(map(num_chg, n_lists))
print(p_list2)

for li in n_lists:
  price = num_chg(li)
  print('금액 :', price)