# pyhon 객체지향 프로그래밍 (oop)

'''
패키지(Package) > 모듈(module) > 클래스(class) > 함수(function)
Function 담을 수 있는 그릇은 class
Class 담을 수 있는 그릇 Module
Module 담을 수 있는 그릇 Package

Objec Oriented Programming (OOP)

Real world          추상화              P/G
object -----------> class -----------> instance
- 명사적 특징 ------- 변수
- 동사적 특징 ------- 함수

class에 정의되는 변수와 함수는 instance의 소유이다
class는 instance 를 생성하기 위해 만든다
'''

# 학생의 정보를 저장한다. --> 비효율적
stuName = '임섭순'
stuMajor = '컴공'
stuId = '1992'
stuGrade = 4.5

# 비효율 극복하려고 시도할수있지만 (list, dict 사용) --> 추천하지 않는 방법
stuNameList = ['임정섭','입섭순']

# class를 이용해서 한 학생의 데이터를 논리적읜 하나의 단위로 묶어서 사용 --> oop
'''
class vs instance
namespace           : 객체를 인스턴승화할 때 저장 된 공간
class variable      : 직접 접근가능 및 공유
instance variable   : 객체소유로 별도 존재
self                : instance 소유의 맴버라는 걸 명시한다 

class
- 함수의 모음
- 역할 : 여러개의 함수와 고유데이터를 묶어서 객체 생성 할 수 있는 템플릿
- 구성 : 맴버 = 변수(데이터) + 매서드(함수), 생성자(초기화)
- 형식 :      class 클래스 이름:
                변수           - 자료저장
                초기화         - 객체생성시 호출되는 함수
                def 함수이름(): - 자료처리
'''

# class 이름의 첫번째 글자는 대문자(capitalize)로 정의하는것이 Rule

class Calc :
    # 변수선언
    x = 0  
    y = 0
    
    # 생성자함수 혹은 초기화
    def __init__(self):
        print('객체 생성시 호출되는 함수이고 난 초기화라고 불리죠')
    
    # 함수선언
    def plus(self):
        print('사용자정의함수이고 전 인스턴스의 소유가 됩니다')

# instance 생성하는 문법
obj = Calc()    # 자동으로 init 객체생성시 호출된 --> 설계도면(class)를 기반으로 건물(instance)를 지은상태
obj.plus()      # 위쪽 obj는 class내 함수들의 주소값을 갖고 있음 그래서 변수명, 함수명 으로 호출 할 수 있음


# 인스턴스 소유의 변수가 아닌 클래스 소유의 변수
# namespace (instance > class > super class)

# OOP 방식으로 설계 하기
class Student :

    def __init__(self, name, major, id, grade):  # 초기화 함수가 생성되는 시점에 4개의 매개변수를 받는다
                                                  # self는 인자가 아님, self는 인스턴스 소유를 나타내느것
        self.name = name                          # 인스턴스 의 소유
        self.major = major 
        self.id = id
        self.grade = grade
        
    def __repr__(self):     # 인스턴스를 문자열로 보여주는 내장함수
        return self.name + "\t" + self.major + "\t" + self.id + "\t" + str(self.grade)
    
    def getInfo(self):
        return '이름 : {} \t 전공 : {} \t 학번 : {} \t 학점 : {}'.format(self.name, self.major, self.id, self.grade)

stuList = []
stu01 = Student('Yoochangho','IE','123123',4.5)
stu02 = Student('Yoochangho02','IE','123123',3.5)
stu03 = Student('Yoochangho03','IE','123123',2.5)

stuList.append(stu01)
stuList.append(stu02)
stuList.append(stu03)

print(stuList)


'''---------------------------------------------------------'''
# 인스턴스 소유의 변수가 아닌 클래스 소유의 변수
# namespace ( instance -> class -> super class )

class student:

    scholarshipRate = 3.5   # --> class varialbe (클래스 소유) self로 사용할 수 없다, class 소유때문에

    def __init__(self, name, major, id, grade):  # 초기화 함수가 생성되는 시점에 4개의 매개변수를 받는다
                                                  # self는 인자가 아님, self는 인스턴스 소유를 나타내느것
        self.name = name                          # 인스턴스 의 소유
        self.major = major
        self.id = id
        self.grade = grade

    def __repr__(self): # 인스턴스를 문자열로 보여주는 내장함수
        return self.name + "\t" + self.major + "\t" + self.id + "\t" + str(self.grade)

    def getInfo(self):
        return '이름 : {} \t 전공 : {} \t 학번 : {} \t 학점 : {}'.format(self.name, self.major, self.id, self.grade)

    def isScholarShip(self):
        if self.grade >= Student.scholarshipRate:
            return True
        else:
            return False

stu01 = Student('ch','babbcb','2016',3.5)
print('장학금 여부 -',stu01.isScholarShip(),Student.scholarshipRate)


# 인스턴스 소유가 아닌 class method
'''
self X
클래스 함수는 cls인 이나를 받고 모든 인스턴스가 공유하는 클래스 변수와
같은 데이터를 생성, 변경 또는 참조하기 위해서 사용 됩니다
'''
class Employee :
    raiseRate = 1.1 # 급여인상률 / class variable 이다 / class 소유의 변수
    def __init__(self,name,salary):
        self.name = name
        self.salary = salary
    def getSalary(self):
        return '현재 {}님의 급여는 {}입니다'.format(self.name, self.salary)

    @classmethod    # @ decorator를 통해 클래스 메서드라는 것을 명시해줘야 한다 # 클래스 소유의 함수
    def updateRate(cls, rate):  # 클래스 소유의 함수(메서드)는 self가 아니라 cls로 가져가야 한다
        print('인상률이 {}에서 {} 로 변경되었습니다.'.format(Employee.raiseRate, rate))
        cls.raiseRate = rate

    def applyRaise(self):   # 인스턴스 소유의 메서드 이기 때문에 아래 Employee 대신에 cls 사용 못한다.
        self.salary = int(self.salary * Employee.raiseRate)

    # static method(함수) cls(클래스소속)도 self(인스턴스)도 아닌것들
    # @ Decoration 필요
    # class 함수와 stactic 함수는 동일한데, 차이는 namesapce(영역)이 다르다는 차이가 있다.

    @ staticmethod
    def isValid(salary):
        if salary < 0 :
            print('음수가 될 수 없습니다')

emp01 = Employee('임정섭',1000)        # 인스턴스 생성
print('연봉 인상 전 급여 - ', emp01.getSalary())   # emp01.getSalary() 는 인스턴스 소유의 함수

Employee.updateRate(1.5)    # Employee.updateRate는 클래스 소유의 함수
emp01.applyRaise()

print('연봉 인상 후 급여 -', emp01.getSalary())

print(Employee.isValid(1000)) # 메서드에 리턴타입이 없는데 print를 하면 None이 된다.