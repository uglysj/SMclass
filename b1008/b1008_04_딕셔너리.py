# 리스트 타입
# 튜플 타입 - 수정이 불가능
# 딕셔너리 타입

dic1 = {
  "번호": 1,
  "이름": "홍길동",
  "kor": 100,
  "eng": 100
}
print(dic1["이름"]) # 출력방법 : 키를 입력하면 값을 출력
# print(dic1["합계"]) # 없는 키를 입력하면 에러
print(dic1.get("이름")) 
print(dic1.get("학번")) # 없는 키를 입럭하면 None, 에러는 나지 않음.
dic1["math"] = 90 # 추가 : 없는 키와 값을 입력하면 추가
dic1['kor'] = 50 # 수정 : 있는 키와 값을 입력하면 수정
del(dic1['eng']) # del(키) 입력하면 삭제
print(dic1)

if dic1.get("이름") != None:
  print(dic1.get("이름"))

# type : class 객체
print(type(dic1.keys()))
# print(type(dic1.keys())[0]) # class 객체 타입이기에 index 값이 없음.

# class 객체 -> list 타입 변경
print(dic1.keys()) # 모든 키 값을 출력
print(list(dic1.keys()))
print(list(dic1.keys())[0])

# 값만 출력 - values
# values() : class 객체 타입
print(dic1.values())
print(list(dic1.values()))

# 모든 키 출력 - keys
for key in dic1.keys():
  print(key, dic1[key])

# 키, 값을 모두 출력
print(dic1.items())
print(list(dic1.items()))

# 키 값만 추출
for key in dic1:
  print(key)

# 값만 추출
for key in dic1:
  print(dic1[key])

# 키, 값을 추출
for key, val in dic1.items():
  print(key, val)

# 평균이 없을 때만 평균을 추가
if '평균' not in dic1:
  dic1['평균'] = 99.0
print(dic1)

a_list = [1, "홍길동", 100, 100, 100, 100, 400, 100.0, 1]
# a_list = [1, 2, 3, "홍길동"]
# print(a_list[0])
# 추가
# append, insert, extend