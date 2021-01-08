
# pyhon 객체지향 프로그래밍 (oop)

'''
패키지(pacake) > 모듈(module) > 클래스(class) > 함수(function)
Objec Oriented Programming (OOP)

Real world          추상화              P/G
object -----------> class -----------> instance
- 명사적 특징 ------- 변수
- 동사적 특징 ------- 함수

'''

# 학생의 정보를 저장하려고 합니다.
stuName = '임섭순'
stuMajor = '컴공'
stuId = '1992'
stuGrade = 4.5

# 추천하지 않는다
stuNameList = ['임정섭','입섭순']

# class를 이용해서 한 학생의 데이터를 논리적읜 하나의 단위로 묶어서 사용
'''
class vs instance
namespace : 객체를 인스턴승화할 때 저장 된 공간
class variable : 직접 접근가능 및 공유
instance variable : 객체소유로 별도 존재

self - instance 소유의 맴버라는 

class
- 함수의 모음
- 역할 : 여러개의 함수와 고유데이터를 묶어서 객체 생성 할 수 있는 템플릿
- 구성 : 맴버 = 변수(데이터) + 매서드(함수), 생성자(초기화)
- 형식 :      class 클래스 이름:
                변수           - 자료저장
                초기화         - 객체생성시 호출되는 함수
                def 함수이름(): - 자료처리
'''

class Calc :
    x = 0
    y = 0

    def __init__(self):
        print('객체 생성시 호출되는 함수이고 난 초기화라고 불리죠')

    def plus(self):
        print('사용자정의함수이고 전 인스턴스의 소유가 됩니다')

# instance 생성하는 문법
obj = Calc()
obj.plus()

# 인스턴스 소유의 변수가 아닌 클래스 소유의 변수
# namespace (instance > class > super class)
class Student :
    scholarshipRate = 3.5  # class variable (클래스 소유)
    def __init__(self, name, major, num, grade):
        self.name = name
        self.major = major
        self.num = num
        self.grade = grade
    def __repr__(self):
        return self.name +"\t"+ self.major +"\t" +self.num +"\t"+ self.str(self.grade) +"\t"
    def getInfor(self):
        return '이름 : {} \t 전공 : {}'.format(self.name, self.major)
    def isScholarShip(self):
        if self.grade >= Student.ScholarShipRate:
            return True
        else:
            return False

stu01 = Student('이중현','기계공학','2020',4.0)
print('장학금 여부 -', stu01.isScholarShip(),Student.scholarshipRate)

stuList = []
stuList.append(Student('입정섭','철학','1992',4.5))
stuList.append(Student('입섭순','컴공','1992',4.5))
stuList.append(Student('섭섭해','경영','1992',4.5))
for stu in stuList :
    print(stu.getInfor())

# 인스턴스 소유가 아닌 class method
'''
self X
클래스 함수는 cls인 이나를 받고 모든 인스턴스가 공유하는 클래스 변수와
같은 데이터를 생성, 변경 또는 참조하기 위해서 사용 됩니다
'''
class Employee :
    raiseRate = 1.1 # 급여인상률 class variable
    def __init__(self,name,salary):
        self.name = name
        self.salary = salary
    def getSalary(self):
        return '현재 {}님의 급여는 {}입니다'.format(self.name, self.salary)

    @classmethod
    def updateRate(cls, rate):
        cls.raiseRate = rate
        print('인상률이 {} 로 변경되었습니다'.format(rate))

    def applyRaise(self):
        self.salary = int(self.salary * Employee.raiseRate)

    # static 함수수
   def isValid(salary):
        if salary < 0 :
            print ('음수가 될 수 없습니다.')

emp01 = Employee('임정섭',1000)
print('연봉 인상 전 급여 - ', emp01.getSalary())
Employee.updateRate(1.5)
emp01.applyRaise()
print('연봉 인상 후 급여 -', emp01.getSalary())
Employee.isValid()