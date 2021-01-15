# List - python sequence type
# 자료구조에서 중요
# 파이썬에서는 배열이 존재하지 않는다.
# 1차원의 자료구조 : R - Vector
# 순서 0 (index 부여 0 ~ ), 중복 0, 수정, 삭제 가능
# [] 이용해서 변수를 선언 할 수 있다.

a = []
a = [1,2,3]
print(a,type(a))    # --> [1, 2, 3] <class 'list'> 출력
print(a[0])         # --> 6 출력
a[0] = 5            # index 0번째의 값을 5 로변경: 1 > 5
print(a)


# 요소 추가하는 함수 : append(), insert(), extend()
# 요소 재배열하는 함수 : sort(), reverse()
# 요소를 삭제하는 함수 : remove(), pop(), del()
# append vs extend 차이

# append() : list 끝에 값 1개만 추가, list 형태의 값이 추가 되면 list 까지 함께 들어감
a = [1,2,3]
a.append([4])
print(a)    # --> [1,2,3,[4]] 출력

# extend() : list 끝에 iterable 의 모든 항목 추가, interable = 4,3,5,6 값만 추가
ex = [4,3,5,6]
a.extend(ex)
print('a - append : ',a)    # --> [1,2,3,4,3,5,6] 출력

# insert : list 맨앞 0 칸에 '6' 추가
a.insert(0,6)
print(a)

# sort() : 요소를 오름차순 크기순으로 재배열 ex) 1,4,2,3 > 1,2,3,4
a.sort()
print(a)

# reverse() : 요소를 내림차순 크기순으로 재배열 ex) 1,4,2,3 > 4,3,2,1
a.reverse()
print(a

# remove : 인수로 부터 전달받은 요소값을 찾아 삭제 한다
Score = [88,95,70,100]
Score.remove(100)   # --> 100 삭제
print(Score)        # --> [88,95,70] 출력

# pop() : 인수로 부터 전달받은 index 번호를 찾아 삭제한다
a = [1,2,3]
print( "a - pop() : ", a.pop(1))    # --> index 1 번째값 2 삭제
print( "a - print : ", a)           # --> [1,3] 출력

# 퀴즈)

# 1.해당 리스트에 '배트맨'을 추가한다면?
moveiRank = ['원더우먼','해리포터','겨울왕구2','가타카','국제수사','반도']
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