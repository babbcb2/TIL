
# python set type - set (집합)
# 순서 x , 중복 x
# {}
# set([])

temp = {'jslim', 'teacher'}
print('set - ', temp, type(temp))

temp = set([1,2,3,4,5,5,5,5,5])
print('set - ', temp, type(temp))

temp = set([1, 3.14, 'pen', False])
print('set - ', temp, type(temp))
casting = tuple(temp)
print('casting - ', casting, casting[1:3],type(casting))

# 교집합 & == intersection() , 합집합 : union(), 차집합 - == difference()
# 객채(변수, 함수)
# 객체.

set01 = set([1,2,3,4,5])
set02 = set([3,4,5,6,7])
print('교집합 & -',set01 & set02)
print('교집합 intersection -',set01.intersection(set02))

print('합집합 | -',set01 | set02)
print('합집합 union -',set01.union(set02))

print('차집합 - -',set01 - set02)
print('차집합 difference -',set01.difference(set02))

# 요소 추가, 삭제(remove(), dicard())
set01.add(7)
print('set add - ', set01)

#set01.remove(9)
#set01.discard(9)

set01.remove(4)
print('set remove - ', set01)

# 중복제거용으로 활용할 수 있음...
gender = ['홀','짝','짝','짝','짝','홀','짝','짝','짝']
setGender = set(gender)
print('du remove - ', setGender)
listGender = list(setGender)
print('list casting - ', listGender, type(listGender))
print('list gender - ', listGender[0])
print('list gender - ', listGender[1])