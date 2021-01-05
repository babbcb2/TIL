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

  

