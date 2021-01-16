# Dict - python mapping type
# Dictionary 는 key 와 value의 대응관계 type
# Hash 또는 Associative Array 와 유사한 구조
# {}
# 순서 x, 키 중복 x, 수정 o, 삭제 o

temp = {}
print(type(temp))

dict01 = {
    'name' : 'changho',
    'age' : 34,
    'address' : 'seoul',
    'birth' : '880218',
    'gender' : 'm'}
print('dict - ', type(dict01), dict01)

# dict 요소를 추가하는 방법
dict01['gender'] = 'w'      # --> gender 값이 m > w 으로 변경
dict01['marriage'] = False  # --> marriage의 key 값과 False value 값이 생성
print('dict - ', type(dict01), dict01)

# 키 유무를 판단
print('marriage' in dict01) # --> key 목록중에 marriage 가 있나요? -> True

# 데이터 확인
print('address - ', dict01['address'])  # --> dict01에 name(key)에 있는 value 를 get 하고싶다
print('name - ', dict01.get('name'))    # --> dict01에 name(key)에 있는 value 를 get 하고싶다

# dict_keys, dict_values , dict_items
print('dict_keys - ', dict01.keys(),type(dict01.keys()))        # --> key 만 출력
print('dict_values - ', dict01.values(),type(dict01.values()))  # --> value 만 출력
print('dict_items - ', dict01.items(),type(dict01.items()))     # --> key, value 출력

# for 구문  -  looping
'''
for (초기식; 조건식; 증감식;)
for item in collection
    statemnet
'''
# key 값만 출력
for key in dict01.keys() :
    print('key : {}'.format(key))

# value 값만 출력
for value in dict01.values():
    print('value : {}'.format(value))

# key, value 출력
for key, value in dict01.items():
    print('key : {}, value : {}'.format(key,value))

# 삭제 pop(), del
print ('dict03 - ', type(dict01), dict01)
del dict01['gender']                        # --> dict01에서 key,value 가 삭제 되었다
print('dict01 del - ', type(dict01),dict01)

