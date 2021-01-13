
# python sequence type - list
# 자료구조에서 중요
# 파이썬에서는 배열이 존재하지 않는다.
# 1차원의 자료구조 : R - Vector
# 순서 0 (index 부여 0 ~ ), 중복 0, 수정, 삭제 가능
# [] 이용해서 변수를 선언 할 수 있다.

a = list()
a = []
a = [1,2,3]

print(a,type(a))
print(a[0])
a[0] = 5
print(a)

# 요소 추가하는 함수 : append(), insert()

a.append(4)
print(a)
a.insert(0,6)
print(a)
a.sort()
print(a)
a.reverse()
print(a)

# pop() : 기존 리스트에서 요소를 가져오고 삭제시킨다.
print( "a - pop() : ", a.pop())
print( "a - print : ", a)

# extend()
ex = [4,3]
a.extend(ex)
print('a - append : ',a)

moveiRank = ['원더우먼','해리포터','겨울왕구2','가타카','국제수사','반도']
# 1.해당 리스트에 '배트맨'을 추가한다면?
moveiRank.append('배트맨')
print('append - 배트맨', moveiRank)
# 2. 원더우먼과 해리포터 사이에 '씽'을 추가한다면?
moveiRank.insert(1,'씽')
print('insert - 씽',moveiRank)
# 3. 리스트에서 '반도'를 삭제한다면?
moveiRank.remove('반도')
print(moveiRank)

# 최대값 최소값 총합 평균
scoreData = [1,2,3,4,5,6,7]
print("max" ,max(scoreData))
print("min" ,min(scoreData))
print("sum" ,sum(scoreData))
print("mean",sum(scoreData)/len(scoreData))