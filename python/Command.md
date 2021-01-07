# python

> 분석 통계 관련 library, OPP
> * Tools(anaconda, pycharm) (IDE)
> * install



### python 장점

- 상대적으로 쉽다
- Interactive programing (대화식 모드)
- 분석, 통계에 관련된 library 풍부하다
- 오픈소스
- R에 비해 범용적



### python 단점

- 하위 호환성이 없다.




### Keyword module loading

* Import_keyword

* Print*keyword.kwlist)



### 변수의 생성 및 삭제

* 변수 (숫자로 시작할수 없다, 특수문자는 _ , $ 만 가능)

* 인터프리터 기반의 언어
* 예약어 변수명으로 사용 불가
  
*  False, def, if, raise, None, del, import, return, True, elif, in, try, and, else, is, while, as, except, ambda, with, assert, finally, nonlocal, yield, break, for, not, class, from, or, continue, global, pass
  
* 변수선언 방법

  * Camel case : 함수정의시 많이 사용하는 방법 numberOfCollage (권장, 많이사용한다)

  * Pascal case : 클래스 정의시 사용하는 방법 NumberOfCollage

  * Snake case : 권장하지 않는다 number_of_cllage

    a = 100

    print(a)



### python data type (built-in types)

* Numeric (int, float / 숫자, 정수, 실수)

* Sequence (list, tuple, range)

* Text sequence (string)

* Mapping (dictionary)

* Set (중복과 순서가 존재하지 않는다. set)

* Boolean (True(T), False(F), not, and, or (논리 연산자, & |, ~(비교연산자))

* Date, timedate (날짜)



### numeric

```
a = 123
b = 3.14
c = 3.14E10

print(type(a)) ==> 123
print(type(b)) ==> 3.14
print(type(c)) ==> 3.14~

div = 3/4
print (div)
==> 0.75

rsult = 3 ** 3
print(rsult)
==> 27

rsult = 10 % 3
print(rsult)
=> 1

rsult = 10 // 3
print(rsult)
==> 3
```



### sequence 

* **`list`**

  * 임의의 값을 순서대로 저장하는 집합 자료형 (index 부여 및 값 변경가능한 형식)

  * 함수를 이용하는 방법과 [ ] 를 이용하는 방법이 있다.

  * range () 이용하여 리스트를 생성하는 방법이 있다.

  * 자료구조에서 중요, 파이썬에서는 배열이 존재하지 않는다.

  * 1차원의 자료구조 : R - Vector

  * 순서 0 (index 부여 0 ~), 중복 0, 수정, 삭제가능

    ```
    a = []
    print (type(a))
    ==> <class 'list'>
    
    a = list()
    print (type(a))
    ==> <class 'list'>
    
    a = [1,2,3]
    print (a)
    ==> [1,2,3]
    ```

* **`tuple`**

  * 순서 o , 중복 o , 수정 x , 삭제 x
  * 읽기 전용 (immutable)
  * () 선언 가능 하다.

  ```
  a = ()
  print(type(a))
  ==> <class 'tuple'>
  
  사용자의 편의를 위해서 괄호없이 만들 수 있다.
  myTuple = 1,2,3,4,5
  multiTuple = (100, 1000, 'Ace','Base','Captine')
  print('tuple print - ',multiTuple)
  
  range01 = range(10)
  print(range01)
  --> 
  
  range02 = range(1, 11, 2)
  print(range02)
  
  even = tuple(range(2, 100, 2))
  print(even)
  even[0] = 1
  ```

* indexing

  ```
  print (a[0])
  print (a[1])
  print (a[2])
  print (a[-1])
  ```

* slicing

  ```
  print(a[0:2])
  ==> [1, 2]
  
  a = [1, 2, 'hello', 3.14]
  a = [1, 2, ['show','me','the','money'], 3.14]
  print(type(a[2]))
  ==> <class 'list'>
  
  print(a[2][2:])
  ==> ['the', 'money']
  
  a = [1,2,3]
  b = [4,5,6]
  print(a+b)
  ==> [1, 2, 3, 4, 5, 6]
  print(a*3)
  ==> [1, 2, 3, 1, 2, 3, 1, 2, 3]
  
  print('p','y','t','h','o','n')
  ==> p y t h o n
  print('p','y','t','h','o','n', sep="")
  ==> python
  print('p','y','t','h','o','n', sep="-")
  ==> p-y-t-h-o-n
  
  seqText = 'Talk is cheap. Show me the code'
  print(seqText[3]) #3번째 칸의 값을 출력
  --> k  
  print(seqText[-1]) #맨 마지막칸의 값을 출력
  --> e  
  print(seqText[0:4]) #0 ~ 3번째 칸의 값을 출력
  --> Talk  
  print(seqText[-6:])  #맨 마지칸으로부터 6번째칸부터 마지칸까지의 값을 출력
  --> e code
  print(seqText[ : : -1]) #값을 역순으로 출력
  --> edoc eht em wohS .paehc si klaT  
  ```

* end

  * 한줄로 출력을 원할경우 맨끝에 end  작성

  ```
  print ('welcome to ', end="")
  print ('IT News')
  ==> welcome to IT News
  ```

* format  사용법 (d, s, f)

* type casting

  ```
  numStr = "720"
  numNum = 100
   
  print (int(numStr) + numNum)  #문자"720"를 int 함수로 숫자 720 으로 수정
--> 820
  print (numStr + str(numNum))  #숫자 100 을 str 함수로 문자 "100" 으로 수정
  --> 720100
  
  year = "2021"
  print(int(year)-1)  #문자"2021"를 int 함수로 숫자 2021 으로 수정
  --> 2020
  ```
  
* set {}

  ```
  setValue = {3,5,7}
  print(type(setValue))
  --> <class 'set'>
  ```

* input ()

  ```
  inputNumber = input('숫자를 입력하세요:')
  print(inputNumber)
  print(type(inputNumber))
  --> 숫자를 입력하세요: (숫자입력)
  ```

* string

  * 문자열 조작을 위한 많은 함수를 제공 하고 있다.

  ```
  아래 문자열에서 '홀'만 출력을 원할경우 
  
  string = '홀짝홀짝홀짝홀짝홀짝'
  print(string[::2])  #첫번째칸으로 시작으로 2칸씩 전진하여 값을 출력한다
  --> 홀홀홀홀홀
  ```

* capitalize

  ```
  string = "python"
  print("capitalize :", string.capitalize())  ##문자의 첫번째단어를 대문자로 출력
  --> Python
  ```

* replace

  ```1
  phoneNumber = '010-1111-2222'
  replacePhoneNumber = phoneNumber.replace('-',"")  #replace '-'삭제후 출력
  print(replacePhoneNumber)
  --> 01011112222
  ```

* split

  ```
  아래 문자열에서 도메인만 출력하고 싶다면?
  
  url = "http://www.naver.com"
  urlSplit = url.split('.')
  print(urlSplit)
  --> ['http://www', 'naver', 'com']  #슬라이싱처리
  
  print('domain:',urlSplit[-1])  #슬라이싱처리 후 맨끝의 값 출력
  --> domain: com
  ```

* strip(), rstrip(), lstrip ()

  * 문자열에서 공백 제거 함수

  ```
  companyName = '   samsung    '
  print(companyName.strip(),len(companyName.strip()))
  print(companyName.rstrip(),len(companyName.rstrip()))
  print(companyName.lstrip(),len(companyName.lstrip()))
  --> 
  samsung 7
     samsung 10
  samsung     11
  ```

* upper(), lower()

  * 대문자, 소문자 변환 함수

  ```
  print(companyName.upper())  #문자 전체를 대문자로 변경
  --> SAMSUNG
  ```

* count(), find(), index()

  * 문자의 빈도  count()
  * 문자 찾기 find()
  * 문자의 인덱스 index()

  ```
  print(len(brandName),brandName.count('c'),brandName.find('f'))
  --> 8 3 -1
  ```

* append(), insert()

  * 요소를 추가하는 함수
  * append() : 맨뒤에  값 추가
  * insert() : 맨 앞에 값 추가 

  ```
  a.append(4)
  print(a)
  --> [5, 2, 3, 4]
  a.insert(0,6)
  print(a)
  --> [6, 5, 2, 3, 4]
  a.sort()
  print(a)
  --> [2, 3, 4, 5, 6]
  a.reverse()
  print(a)
  --> [6, 5, 4, 3, 2]
  
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
  --> 
  append - 배트맨 ['원더우먼', '해리포터', '겨울왕구2', '가타카', '국제수사', '반도', '배트맨']
  insert - 씽 ['원더우먼', '씽', '해리포터', '겨울왕구2', '가타카', '국제수사', '반도', '배트맨']
  ['원더우먼', '씽', '해리포터', '겨울왕구2', '가타카', '국제수사', '배트맨']
  ```

* max, min, sum

  * 최대값, 최소값

  ```
  scoreData = [1,2,3,4,5,6,7]
  print("max" ,max(scoreData))
  print("min" ,min(scoreData))
  print("sum" ,sum(scoreData))
  --> 
  max 7
  min 1
  sum 28
  ```



### mpping type

* dict

  * dictionary 는 key 와 value의 대응 관계 type
  * Hash 또는 Associative Array 와 유사한 구조
  * {}
  * 순서 x , 키 중복 x , 수정 o , 삭제 o

  ```
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
  
  --> 
  <class 'dict'>
  dict -  <class 'dict'> {'name': 'seop', 'age': 49, 'address': 'kwangju', 'birth': '730910', 'gender': 'm'}
  
  dict 요소를 추가하는 방법
  dict01['marriage'] = True
  print('dict - ', type(dict01), dict01)
  --> 
  dict -  <class 'dict'> {'name': 'seop', 'age': 49, 'address': 'kwangju', 'birth': '730910', 'gender': 'm', 'marriage': True}
  ```

* keys , values , items

  ```
  print('dict_keys - ', dict01.keys(),type(dict01.keys()))
  --> 
  dict_keys -  dict_keys(['name', 'age', 'address', 'birth', 'gender', 'marriage']) <class 'dict_keys'>
  
  
  print('dict_values - ', dict01.values(),type(dict01.values()))
  -->
  dict_values -  dict_values(['seop', 49, 'kwangju', '730910', 'm', True]) <class 'dict_values'>
  
  
  print('dict_items - ', dict01.items(),type(dict01.items()))
  -->
  dict_items -  dict_items([('name', 'seop'), ('age', 49), ('address', 'kwangju'), ('birth', '730910'), ('gender', 'm'), ('marriage', True)]) <class 'dict_items'>
  ```

* looping

* for 문

  ```
  for item in collection
  
  for key in dict01.keys() :
      print('key : {}, value : {}'.format(key,dict01.get(key)))
  -->
  key : name, value : seop
  key : age, value : 49
  key : address, value : kwangju
  key : birth, value : 730910
  
  for value in dict01.values():
      print('value : {}'.format(value))
  -->
  value : seop
  value : 49
  value : kwangju
  value : 730910
  value : m
  value : True
  
  for (key, value) in dict01.items():
      print('key : {}, value : {}'.format(key,value))
  -->
  key : name, value : seop
  key : age, value : 49
  key : address, value : kwangju
  key : birth, value : 730910
  key : gender, value : m
  key : marriage, value : True
  ```

* del

  * 삭제

  ```
  print ('dict03 - ', type(dict01), dict01)
  del dict01['gender']
  print('dict01 del - ', type(dict01),dict01)
  --> 
  dict03 -  <class 'dict'> {'name': 'seop', 'age': 49, 'address': 'kwangju', 'birth': '730910', 'gender': 'm', 'marriage': True}
  dict01 del -  <class 'dict'> {'name': 'seop', 'age': 49, 'address': 'kwangju', 'birth': '730910', 'marriage': True}
  ```

  

### set type

> 순서 x , 중복 x  /  {}  /  set ([])

```
temp = {'jslim', 'teacher'}
print('set - ', temp, type(temp))
--> set -  {'teacher', 'jslim'} <class 'set'>

temp = set([1,2,3,4,5,5,5,5,5])
print('set - ', temp, type(temp))
--> set -  {1, 2, 3, 4, 5} <class 'set'>  # 중복된 5 값 하나만 출력

temp = set([1, 3.14, 'pen', False])
print('set - ', temp, type(temp))
casting = tuple(temp)
print('casting - ', casting, casting[1:3],type(casting))
--> 
set -  {False, 1, 3.14, 'pen'} <class 'set'>
casting -  (False, 1, 3.14, 'pen') (1, 3.14) <class 'tuple'>
```

* intersection, union, difference

> 교집합 & == intersection() , 합집합 : union () , 차집합 - 

```
set01 = set([1,2,3,4,5])
set02 = set([3,4,5,6,7])
print('교집합 & -',set01 & set02)
print('교집합 intersection -',set01.intersection(set02))
--> 
교집합 & - {3, 4, 5}
교집합 intersection - {3, 4, 5}

print('합집합 | -',set01 | set02)
print('합집합 union -',set01.union(set02))
-->
합집합 | - {1, 2, 3, 4, 5, 6, 7}
합집합 union - {1, 2, 3, 4, 5, 6, 7}

print('차집합 - -',set01 - set02)
print('차집합 difference -',set01.difference(set02))
--> 
차집합 - - {1, 2}
차집합 difference - {1, 2}
```

* 요소추가, 삭제(remove(), discard()

```
set01 = set([1,2,3,4,5])
set01.remove(4)
print('set remove - ', set01)
--> 
set remove -  {1, 2, 3, 5}

# 중복제거용으로 활용할 수 있음...
gender = ['홀','짝','짝','짝','짝','홀','짝','짝','짝']
setGender = set(gender)
print('du remove - ', setGender)
--> du remove -  {'짝', '홀'}  # 중복이 되지 않아 짝, 홀 만 출력 됨

listGender = list(setGender)  # {짝, 홀} 으로 구분되어 져있는 set list 형태로 인덱스로 분류
print('list casting - ', listGender, type(listGender))  # list 로 변경
print('list gender - ', listGender[0]) --> 짝  # 인덱스 0 출력
print('list gender - ', listGender[1]) --> 홀  # 인덱스 1 출력
```



### Bool type

> True(T), False (F)
>
> not , and , or --> 논리 연산자
>
> & , | , ~  --> 비교 연산
>
> Fasle 으로 간주 되는 상황
>
> "", [], (), {}, 숫자(0이외의 숫자는 True),  None

```
xValue = 5  # 0101
yValue = 0  # 0000  -> 0000 -> 0
            #       -> 0101 -> 5

print(xValue & yValue) --> 0  # 0101 & 0000
print(bool(xValue&yValue)) --> False  #
print(xValue | yValue) --> 5
print(bool(xValue | yValue)) --> True


trueValue = True
falseValue = False

print(int(trueValue))  --> 1
print(int(falseValue))  --> 0

print(trueValue & falseValue)	--> False
print(trueValue | falseValue)	--> True

print ('and - ' , trueValue and falseValue)		--> and -  False
print ('or - ' , trueValue or falseValue)		--> or -  True
print ('not - ' , not trueValue)				--> not -  False
```



### date type

```
from datetime import date, datetime
이거는 datetime 패키지에서 date와 datetime 모듈들을 가져오겠다. 라는 의미입니다.

today = date.today()
print('date -',type(today), today, today.year, today.month, today.day)
print('{} 년도, {} 월, {} 일'.format(today.year,today.month, today.day))
--> 
date - <class 'datetime.date'> 2021-01-06 2021 1 6
2021 년도, 1 월, 6 일

# 시간
todayDateTime = datetime.today()
print('datetime -', todayDateTime)
print('{} 시 , {} 분, {} 초'.format(todayDateTime.hour, todayDateTime.minute, todayDateTime.second))
-->
datetime - 2021-01-06 17:03:40.570948
17 시 , 3 분, 40 초

from datetime import  date, timedelta
from dateutil.relativedelta import relativedelta
today = date.today()
days = timedelta(days=-1)
print('오늘 이전 하루 - {}'.format(today+days))
--> 오늘 이전 하루 - 2021-01-05

# year, month 관련된 옵션을 필요로 하신다면
# relativedelta

months = relativedelta(months=-2)
print('두달 전 오늘 - {}'.format(today+months))	--> 두달 전 오늘 - 2020-11-06


from dateutil.parser import parse

userDate = parse("2021-06-04")
print('parse date -', userDate)		--> parse date - 2021-06-04 00:00:0

userDate = datetime(2021, 12, 25)
print('datetime -', userDate, type(userDate))
--> datetime - 2021-12-25 00:00:00 <class 'datetime.datetime'>

# 날짜 객체의 출력형식을 원하는 것으로 변경
today = datetime.today()

# 날짜형식 -> 문자열 형식의 포맷으로 지정
# strftime()
print("{}".format(today.strftime('%m-%d-%y')))

# 문자열형식 -> 날짜형식 (strptime)

strDate = '2021,01,06-11:12:40'
userDate = datetime.strptime(strDate,'%Y,%m,%d-%H:%M:%S')
print(type(userDate),userDate)
```



### control statement

> if (조건문), for(반복문), while (반복문)

```
# 사용자 입력 함수
# input()

name = input("Enter your Name :")
grade = input("Enter your Graed :")
company = input("Enter your Company :")
print(name, grade, company)

# 입력된 값을 2로 나누었을때 남은 숫자가 0 이면 짝수, 1 이면 홀수
# if 조건 입력
# else : if 조건이 맞지 않으면 해당 명령문 실행

inputNumber = int(input("Enter your digit(1~100) :"))
# print(inputNumber%2 == 0)
if inputNumber%2 == 0 :		
    print('짝수입니다.')
else:
    print('홀수입니다.')

# 값이 3의 배수인지 5의 배수인지 판별하고 싶다면?
number = 15
if (number%3 == 0 & number%5 == 0):
    print('{}은 3과 5의 배수입니다.'.format((number)))
else:
    print('{}은 3과 5의 배수가 아닙니다.'.format((number)))
--> 15은 3과 5의 배수입니다.

# if ~ elif
if number%3 == 0:
    print('{}은 3의 배수입니다'.format(number))
elif number%5 == 0:
    print('{}은 5의 배수입니다'.format(number))
else:
    print('{}은 3과 5의 배수가 아닙니다'.format(number))
--> 15은 3의 배수입니다

# 윤년의 조건
# 4의 배수이고, 100의 배수가 아니거나
# 400의 배수일 때를 윤년으로 본다면
# if 구문을 사용하여 년도와 월을 입력받아서 월의 마지막 일을 출력한다면?

year = 2020
if year%4 == 0 and year%100 != 0 or year%400 == 0 :
    print('{}는 윤년입니다'.format(year))
else:
    print('{}는 윤년이 아닙니다'.format(year))


# 윤년 체크 / 윤년이라면 마지막 2월의 마지막일을 체크
year = int(input('년도를 입력하세요 :'))
month = int(input('달을 입력하세요 :'))

year_month      = [31,28,31,30,31,30,31,31,30,31,30,31]
leap_year_month = [31,29,31,30,31,30,31,31,30,31,30,31]

if year%4 == 0 and year%100 != 0 :
    print('{}년, {}월의 마지막 일은 {} 입니다'.format(year, month, leap_year_month[month-1]))
elif year%400 == 0:
    print('{}년, {}월의 마지막 일은 {} 입니다'.format(year, month, leap_year_month[month-1]))
else:
    print('{}년, {}월의 마지막 일은 {} 입니다'.format(year, month, year_month[month-1]))
-->
년도를 입력하세요 :>? 2020
달을 입력하세요 :>? 5
2020년, 5월의 마지막 일은 31 입니다

# if ~ in
areaKeyDict = {'서울':100, '광주':200}
region = '부산'
if region in areaKeyDict :		## areaKeydict 값을 가져와 region 의 값이 있을경우 pass
    pass						## region 의 값이 없을경우 '{region}값이 존재하지 않습니다. 출력 '
else:
    print ('{}값이 존재 하지 않습니다'.format(region))
--> 부산값이 존재 하지 않습니다

# 삼항 연산자
num      = 9
result   = 0
result = num * 2 if num > 5 else num + 2
print('삼항 연산자',result)
--> 만약, num의 값이 5를 초과할경우 num *2 곱해라, 아닐경우 num +2 를 해라
--> (결과)if (조건) else (아닐경우)
```



### control statement for looping

> for ~ in range(start index, end index, step)
>
> for ~ in list, dict

* for

```
userSum = 0
for tmp in range(1, 11) :
    # print(tmp, end="\t")
    print(tmp)
    userSum += tmp
print('누적값은 : {} 입니다.'.format(userSum))

--> tmnp 라는 단어는 예악어 이고, tmp 의 값은 1 ~ 10 까지 이다.
--> userSum += tmp 는 tmp 의 값을 모두 더하라는 명령어
--> print 할경우 누적값은 55 입니다.
```

* 

