# python

> 분석 통계 관련 library, OPP
> * Tools(anaconda, pycharm) (IDE)
> * install



### python 장점

- 상대적으로 쉽다
- Interactive programing
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

print(type(a))
print(type(b))
print(type(c))

div = 3/4
print (div)

rsult = 3 ** 3
print(rsult)

rsult = 10 % 3
print(rsult)

rsult = 10 // 3
print(rsult)
```



#### sequence 

* **`list`**

  * 임의의 값을 순서대로 저장하는 집합 자료형 (index 부여 및 값 변경가능한 형식)

  * 함수를 이용하는 방법과 [ ] 를 이용하는 방법이 있다.

  * range () 이용하여 리스트를 생성하는 방법이 있다.

    ```
    a = []
    print (type(a))
    a = list()
    print (type(a))
    a = [1,2,3]
    print (a)
    #indexing
    print (a[0])
    print (a[1])
    print (a[2])
    print (a[-1])
    ```

* 

  a = []
  print (type(a))
  a = list()
  print (type(a))
  a = [1,2,3]
  print (a)

* **`tuple`**

  ```
  a = ()
  
  print(type(a))
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
  
  a = [1, 2, 'hello', 3.14]
  a = [1, 2, ['show','me','the','money'], 3.14]
  print(type(a[2]))
  print(a[2][2:])
  
  a = [1,2,3]
  b = [4,5,6]
  print(a+b)
  print(a*3)
  
  print('p','y','t','h','o','n')
  print('p','y','t','h','o','n', sep="")
  print('p','y','t','h','o','n', sep="-")
  ```

  

* end

  ```
  print ('welcome to ', end="")
  print ('IT News')
  ```



* format  사용법 (d, s, f)

* type casting

  ```
  a = list(a)
  
  print(type(a))
  ```

  