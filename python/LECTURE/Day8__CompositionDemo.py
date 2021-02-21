
'''
학습목표
- Composition == Aggregation
- 상속을 피하고 클래스의 일부 기능을 그대로 활용하고 싶을때
- File 입출력
'''

class Calc01(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def add(self):
        return self.x + self.y
    def subtract(self):
        return self.x - self.y

class Calc02(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def add(self):
        return self.x + self.y
    def multiply(self):
        return self.x * self.y

class UserCalc :
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.cal02 = Calc02(x,y) # 객체를 명시적으로 생성

    def add(self):
        return self.x + self.y
    def subtract(self):
        return self.x - self.y
    def multiply(self):
        return self.cal02.add()

calc = UserCalc(3,4)
print('calc multiply -', calc.multiply())

'''
- 예외(Exception) - SyntaxError, TypeError, NameError, IndexError, ValueError, KeyError ...
- 처리할 수 있는 구문
try     :
    에러가 발생 할 가능성이 있는 코드
except  :
    1. 프로그램의 흐름을 정상으로 컨트롤 하는 코드가 들어가거나
    2. 예외발생의 디버깅
    3. 로그파일을 만들어서 예외정보를 저장
except  :
    발생된 에러를 잡기위한 객체 정의
else    :
    에러가 발생되지 않을 때 실행되는 블럭
finally :
'''

#print('error)
# a = 10
# b = 20
# print(c)
# print(100/0)
# print('*', * 50)
# print('end')

# 에외가 없는 것을 가정하고 프로그램 작성 -> 런타임 예외 발생시 예외처리를 권장

def userKeyIn():
    try :
        age = int(input('본인의 나이를 입력하세요'))
    except Exception as e :
        print('문자열이 아닌 정수를 입력해 주세요')
    else :
        print('age -',age)
        print('함수 실행 종료')
    finally:
        print('넌 너무 지조가 없다.. 항상 실행되니까!!')
userKeyIn()


nameList = ['kim', 'lee', 'pack', 'lim']
try:
    name = str(input('Enter your name?'))
    idx = nameList.index(name)
except ValueError as e:
    print('{} Not Found it !'.format(name, idx+1))
else:
    print('{} Found it !'.format(name))
finally:
    print('예외 여부와 상관없이 항상 실행되는 블럭')

print('프로그램 종료')

# 사용자 정의 예외 클래스를 작성
class InsufficientError(Exception):
    def __init__(self, msg):
        self.msg = msg


# 클래스에 정의된 함수에 예외처리 적용 및 강제 예외 발생

class Account :
    def __init__(self, account, balance, intertestRate):
        self.account = account
        self.balance = balance
        self.intertesetRate = intertestRate

    def withDraw (self, amount) :
        try:
            if self.balance < amount :
                raise InsufficientError('잔액이부족합니다~')
        except Exception as e:
            print('Error msg-', str(e))
        else:
            self.balance -= amount

    def withDraw02 (self, amount) :
        if self.balance < amount :
            raise InsufficientError('잔액이부족합니다~')
        else:
            self.balance -= amount

account = Account('100', 100000, 0.073)
try :
    account.withDraw02(200000)
except InsufficientError as e:
    print(str(e))
print('프로그램종료')

'''
객처생성 - 클래스 (변수, 함수)
클래스없이 객체를 생성하는 방법(변수)
class A :
    def __init__(self,x) :
        self.x = x
usage)
collections.namedtuple('클래스 이름', (변수) [변수] )
'''
import collections

Person = collections.namedtuple('Person',['name','id'])
per = Person('JSIM','100')
print(per,type(per))

# 속성에 접근
print('idx 0-', per[0])
print('idx 0-', per[1])

for idx in range(len(per)):
    print('idx {} {} '.format(idx, per[idx]))

# 속성에 접근 2
print(per.name)
print(per.id)

# 속성에 접근 3
name, id = per
print(name, id)

'''
1. 직장인 이름, 나이, 부서를 속성으로 갖는 클래스 만들기
2. 직장인 이름, 나이, 부서를 속성으로 갖는 클래스를 namedtuple 만들기

collections.namedtuple('클래스 이름', (변수) [변수] )
'''

Emp = collections.namedtuple('Emp',['name','age','dept'])
emp01 = Emp('jslim','28','edu')
print(emp01.name,emp01.age,emp01.dept)

