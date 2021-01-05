
# python mapping type - dict
# dictionary 는 key 와 value의 대응관계 type
# Hash 또는 Associative Array 와 유사한 구조
# {}
# 순서 x, 키 중복 x, 수정 o, 삭제 o

temp = {}
print(type(temp))

dict01 = {
    'name' : 'seop',
    'age' : 49,
    'address' : 'kwangju',
    'birth' : '730910',
    'gender' : 'm',
}
print('dict - ', type(dict01), dict01)

# dict 요소를 추가하는 방법
dict01['marriage'] = True
print('dict - ', type(dict01), dict01)

# 키 유무를 판단
print('marriage' in dict01)

# 데이터 확인
print('address - ', dict01['address'])
print('name - ', dict01.get('name'))

# dict_keys, dict_values , dict_items
print('dict_keys - ', dict01.keys(),type(dict01.keys()))
print('dict_values - ', dict01.values(),type(dict01.values()))
print('dict_items - ', dict01.items(),type(dict01.items()))

# looping
'''
for item in collection
    statemnet
'''

for key in dict01.keys() :
    print('key : {}, value : {}'.format(key,dict01.get(key)))

print(dict01.get(key))


for value in dict01.values():
    print('value : {}'.format(value))

for (key, value) in dict01.items():
    print('key : {}, value : {}'.format(key,value))

# 삭제 pop(), del
print ('dict03 - ', type(dict01), dict01)
del dict01['gender']
print('dict01 del - ', type(dict01),dict01)

