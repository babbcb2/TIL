# Tuple - python sequence type
# 순서 o, 중복 o, 수정 x, 삭제 x
# 읽기 전용 (immutable)
# () 선언 가능하다

myTuple = ('반도','강철비2','아이언맨')
oneTuple = (1,)

# 사용자의 편의를 위해서 괄호없이 만들 수 있다.
myTuple = 1,2,3,4,5
multiTuple = (100, 1000, 'Ace','Base','Captine')        # ()괄호 안의 값들이 tuple 형태로 정의 됨
print('tuple print - ',multiTuple, type(multiTuple))
# tuple print -  (100, 1000, 'Ace', 'Base', 'Captine') <class 'tuple'> 으로 출력되고있음


# indexing
multiTuple = (100, 1000, 'Ace','Base','Captine')
print('index 1 - ', multiTuple[1])  # --> index 1번째 값 출력 : 1000
print('slicing - ', multiTuple[2:], type(myTuple[2:]))  # --> index 2번째 값부터 출력 : Ace, Base, Captine


# casting
multiList = list(multiTuple[2:])
castingMultituple = tuple(multiList)

# 1 ~ 99 까지의 정수 중 짝수만 저장 된 튜플을 생성한다면?
range01 = range(10)
print(range01)

range02 = range(1, 11, 2)
print(range02)

even = tuple(range(1, 100, 2))  # 범위 1부터 99까지의 숫자 중에 1 + 2 step 씩 값을 출력
print(even)
 even[0] = 1
#even[0] = 1  --> error

print(7 in range02)
print(10 in range02)
print(range02.index(7))
print(range02[2:])
print(range02[-1])