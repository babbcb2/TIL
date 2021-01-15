# 변수선언 방법 3가지
# camel case: 함수정의시 많이 사용 =numberOfCollageGraduates
# pascal case: 클래스 정의시 =NumberOfCollageGraduates
# snake case: number_of_collage_graduates

# 출력
a = 100
print(a)
# del a : a의 정이를 지움


# 파이썬의 데이터 타입 (built-in types)
# numeric : 정수,실수
# sequence : list, tuple, range
# text sequence : str
# mapping : dict
# set : set (중복과 순서가 정의되지 않음)
# bool : true(t), false(f), not, and, or(논리연산자) / , &,: ~(비교연산자)
# date, timedate : 날짜


# numeric(숫자, 정수, 실수)
a = 123
b = 3.14
c = 3.14E10 #==> 지수
d = 0o34 #==> 8진수
e = 0xab #==> 16진수
print(a,b,c,d,e)


# type() --> 어떤형태의 타입인지 알아볼때 사용
print(a)

div = 3/4       # --> 나누기
print(div)

result = 10//3  # --> 몫
print(result)

rsult = 3 ** 3  # --> 자승
print(rsult)

rsult = 10 % 3  # --> 나머지 값
print(rsult)


# list
# 임이의 객체를 순서대로 저장하는 집합 자료형
# 보편적으로 사용하는 방법
a = []
print (type(a))
a = [1,2,3]
print (a)


#indexing
#index = 0   1   2
#        |   |   |
   a = [ 1 , 2 , 3 ]
print(a[0])     # --> index 0번째 값
print(a[1])     # --> index 1번째 값
print(a[2])     # --> index 2번째 값
print(a[-1])    # --> index 맨뒤 1번째값부터 시작
print(a[-2])    # --> index 맨뒤 2번째값부터 시작
print(a[-3])    # --> index 맨뒤 3번째값부터 시작


# seperator
a = 'apple'
b = 'banana'
c = 'melon'
print(a, b, c, sep='!')
print(a, b, b, c, sep='\n')
print('p','y','t','h','o','n')
print('p','y','t','h','o','n', sep="")
print('p','y','t','h','o','n', sep="-")
#참고 : Escape 코드
# \n : 개행
# \t : 탭
# \\ : 문자
# \' : 문자
# \" : 문자
# \000 : 널 문자


# end
print('welcome to' , end='')  # end 다음 출력 print 와 함께 출력
print('it news' , end='')
print('web sites' , end='')


# slicing
a = ('slicing')
print(a[0:2])       # --> sl 만 출력 (index 0~1까지의 값 출력)
print(a[0:1])       # --> s  만 출력 (index 0 까지의 값 출력)


#format 사용법(d, s, f)
one = 1
two = 2
print(one,two)
print('첫번째 값- {}, 두번째 값 - {}'.format(one, two))   # --> one, tow 값을 {} {} 순서에 맞게 출력


# tuple
score = (88,95,70,100,99)
print(type(score))

