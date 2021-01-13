# python function

'''
함수는 가독성을 높이기 위한 방법으로
하나 이상의 본문을 가지는 코드는 함수로 정의 하는 것이 좋다
내장함수 | 사용자정의 함수
함수를 정의할 때는 def 키워들 리용해서 함수를 정의
'''

# user define function
'''
def functionName():
    statement
    return value(built-in type)
'''

#def userPrint():
#print('userprint')

#from digital.python import packageFunction
#packageFunction.printCoins()

from digital.python import packageFunction as f
rtnMsg = f.returnFunc()
print('call returnFunc -',rtnMsg)

echoMsg = f.sayEcho('섭섭님')
print('call sayEcho() -',echoMsg)

domain = f.makeUrl('naver')
print('call makeUrl -', domain)

f.badFunc('jslim')

turRtn = f.tupleFunc(1,2,3,4,5,6,7,8,9)
print('call tupleFunc -', turRtn)

f.dictFunc(name='jslim', age = 49)

(oddSum ,evenSum) =f.cntSum(100, 500)
print('홀수의 합{}, 짝수의 합{}'.format(oddSum,evenSum))

# 인자값으로 넘겨받은 년도 사이의 윤년을 찾아 리턴시켜주는 함수를 작성
# list type
leapYearList = f.leapYearFunc(1900, 2021)
print('leapYearList - ', leapYearList)

dictMsg = f.rtnDictFunc(10)
print('dictMSG - ', type(dictMsg), dictMsg)

for value in dictMsg.values() :
    print('dictValues - ', value)

for key in dictMsg.keys() :
    print('dictKeys - ', key)

# default parameter 사용
# worker function
def defaultParam (x,y,z = True):
    paraSum = x + y
    if paraSum > 10 and z :
        return paraSum
    else:
        return 0

#caller function
result = defaultParam(10, 20)
print ('caller defaultParam() -', result)

# 함수의 입력 인자가 list, dict - mutable(참조가능하다)
# 함수의 입력 인자가 숫자, 문자열, tuple - immutable (참조가 불가능하다)
tmpList = [10]
tmpX = 10
def mutableFunc(argX,argList):
    argX = argX+100
    argList.append(100)

mutableFunc(tmpX, tmpList)
print('tmpList -', tmpList)
print('tmpX -', tmpX)

# variable(변수) - 선언위치에 따라서 (local, global)
tmp = 100  # global 변수
def myFunc(x) :
    tmp = 0  # local변수 (global보다 우선권을 가지게 된는다)
    tmp += x
    return tmp

print('call myFunc -', myFunc(100))

def persionInfo() :
    pass

def personInfo(weigth, height, **other):
    print('weight -', weigth)
    print('height -', height)
    print('extra -', other, type(other)) #dict

personInfo(54, 177, name='유창호', address='seoul')

def overroll(args01, args02, *args03, **args04):
    print(args01, args02, *args03, **args04)

overroll(10,20,'lee','kim','pack','cho', args01=10, args02=20, arg03=40)

# nested function (중첩함수)
def outerFunc(num):
    def innerFunc(num):
        print('innerFunc -', num)
    innerFunc(num + 100)

outerFunc(200)
# innerFunc(100) - 실행불가 즉, 호출불가합니다

'''
중첩함수 활용 예)
outer 함수 : 자료(data) 생성, inner 함수 포함
inner 함수 : 자료 연산/처리(합계, 평균)

중첩함수..
그 호출과 실행이라는걸로 놓고볼 때..
outer를 호출을 하고 있지만 내부에 '실행' 구문이 없죠 
한줄씩 순차적으로 연산하기 때문에 def inner가 호출이 되죠. 실행이 아니라? 
현재 로직보면 호출, (호출 - 실행), 실행 이렇게 되어있으니 outer에서 실행하는 구문인
innerFunc(num + 100)을 통해inner를 실행! 하는거죠 그래서 inner가 실행됨에 따라
inner 자체에 있는 호출이 되고 실행이 되는거구.
'''
def calFunc(data) :
    dataset = data
    def sumFunc():
        total = sum(dataset)
        return total
    def avgFunc():
        avg = total / len(dataset)
        return avg
    return sumFunc(), avgFunc()

data = list(range(1,101))
print('range data -', data)

(rtnSumFunc, rtnAvgFunc) = calFunc(data)
tot = rtnSumFunc()
print(tot)
avg = rtnAvgFunc(tot)
print(avg)

'''
재귀함수(self-recursive function)
- 함수 내부에서 자신의 함수를 반복 호출하는 기법
- 용도 : 반복적으로 변수를 변경해서 연산할 떄 (누적, 팩토리얼)
'''

def countFunc(n): # n = 5 -> 1, 2, 3, 4, 5
    if n == 0:
        return 0
    else:
        countFunc(n-1) #stack [5,4,3,2,1]
        print(n, end="")

countFunc(5) # 1 2 3 4 5
countFunc(0) # 0

# 누적 : (n) = 1+ 2 + 3 + ... + n
def addSum(n):
    if n == 1:
        return 1
    else:
        result = n + addSum(n-1)
        print('debug -',result)
        return result

print('n=5', addSum(5))
print('n=100 -', addSum(100))

# 익명의 함수(lambda 식)을 만드는 방법
# 람다식 (가독성 향상, 코드 간결, 메모리 절약- 즉시 실행 함수이기

def multiFunc(x,y):
    return x * y

print(multiFunc(10, 50))

# syntac : lambda arg : body

lambdaVar = lambda x,y : x * y
print(lambdaVar(10,50))

def lambdaFunc(x,y,func):
    print('lambdaFunc -', x * y * func(100,100))

lambdaFunc(10,20,lambda x,y : x * y)
lambdaFunc(10, 20, lambdaVar)
lambdaFunc(10, 20, multiFunc)

# hint
def totalLengthFunc (word:str, num:int):
    return len(word) * num

print('hint -', totalLengthFunc('i love you', 10))