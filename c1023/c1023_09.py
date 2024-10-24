# 금액이 80000원 미만 항공권 출력
# 김포 - 제주 80000원 이하 항공권 개수
# 제주 - 김포 80000원 이하 항공권 개수
from bs4 import BeautifulSoup

with open('c1023/flight.html', 'r+', encoding='UTF-8') as f:
  soup = BeautifulSoup(f, 'lxml')
data = soup.select_one('#__next > div > main > div.domestic_flight_content__vYDHd > div > div.domestic_results__gp5WB')
lists = data.select('div.domestic_Flight__8bR_b')
print('[ 김포 - 제주 편도 항공편 ]')
for idx, list in enumerate(lists):
  price = int(list.select_one('i.domestic_num__ShOub').text.replace(',',''))
  times = list.select('b.route_time__xWu7a')
  if price <= 80000:
    print(f"{idx + 1}.")
    print('항공사 :', list.select_one('b.airline_name__0Tw5w').text.strip())
    print('출발시간 :', times[0].text.strip(), '도착시간 :', times[1].text.strip())
    print('가격 :', price)
    print('-' * 30)
  else:
    print(f"{idx + 1}. 조건미달")
    continue