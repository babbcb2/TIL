'''
oop
- 상속 ( is ~ a )
- 다형성
- 은닉화
- 추상화
lib - has ~ a 관계, is ~ a 관계

파이썬
object  - data
        - function
'''

class Car :
    def __init__(self,name,door,cc):    # 기본생성자 = 스폐셜생성자 = 인스턴스소유
        self.name = name
        self.door = door
        self.cc   = cc

    def carInfo(self):
        print('%s는 %d cc이고, 문짝은 %d개 입니다' % (self.name,self.cc,self.door))

car01 = Car('GV70', 4, 2400)
car01.carInfo()
# car01.함수 # car01 함수에 접근
# car01.변수 # car01 변수에 접근


# 최상위 : Object > Sup > Sub 순 Sub 가 가장 많은 구성요소를 갖고있다.
class Sup (object):   # Sup 가 object 를 상속받는 형식 java의 extends
    pass

class Sub(Sup):   # Sub 가 sup 를 상속 받는 형식
    pass


class Parent(object):
    
    # 초기화 함수, 생성자
    def __init__(self, name , job):
        self.name = name
        self.job  = job

    def display(self):  # repr 와 똑같은 내장함수, 인스턴스 주소값이 아닌 문자열을 출력한다
        return '당신의 이름은 {} 이고, 직업은 {} 입니다'.format(self.name,self.job)

class Child01(Parent):  # Parent 를 상속받는 Childe01
    def __init__(self, name, job, age):
        self.name = name
        self.job  = job
        self.age  = age
    def childInfo(self):
        print('당신의 이름은 {} 이고, 직업은 {} 이며 나이는 {} 입니다'.format(self.name,self.job,self.age))

class Child02(Parent):
    pass

# 상속을 활용한 예:
class Person(object):
    def __init__(self, name, age, address):
        self.name = name
        self.age  = age
        self.address = address
    def perInfo(self):
        return self.name +"\t"+ str(self.age) +"\t"+ self.address
                                # 문자열 중간에 int 형 즉, 다른 타입이 있으면 Error 발생한다
                                # type casting 필요

# super() : 부모의 생성자를 호출하는 작업
# StudentVO, TeacherVO 2개의 자식클래스. 둘다 Parent class 를 상속 받고 있다

class StudenVO(Person):
    def __init__(self, name, age, address, stuId):  # 4개의 값중 3개는 Person에게서 가져옴
        super().__init__(name, age, address)    # 부모의 __init__ 생성자를 호출하는 행위, 자식에게 들어온 인자를 부모에게 assign 하는 행위
        self.stuId = stuId      # self로 자식 클래스에서 추가로 정의한 studID 를 assign

    def stuInfo(self) :
        return super().perInfo() + "\t" + self.stuId # 부모의 함수인 perInfo를 가져오고 자식의 것인 stuId를 합친것

    def perInfo(self):
        return super().perInfo() +"\t"+ self.stuId  # 부모의 함수인 perInfo를 가져오고 자식의 것인 stuId를 합친것

class TeacherVO(Person):
    def __init__(self, name, age, address, subject):
        super().__init__(name, age, address)
        self.subject = subject

    def teaInfo(self) :
        return super().perInfo() + "\t" + self.subject

    def perInfo(self) :
        return super().perInfo() + "\t" + self.subject

class ManagerVO(Person) :
    def __init__(self, name, age, address, dept):
        super().__init__(name, age, address)
        self.dept = dept

    def empInfo(self):
        return super().perInfo() + "\t" + self.dept

    def perInfo(self) :
        return super().perInfo() + "\t" + self.dept


# encapsulation(은닉화)
# information hiding(정보은닉)
# 변수에 대한 직접적인 접근을 막고자 변수앞에 __ 처리를 통해 캡슐화를 시켜줄 수 있다.

class MyDate(object) :
        # def __init__이 없다면
        # 인자가 없는 init이 삽입된 코드라고 간주함

    def setYear(self, year):
        if year < 0 :
            self.__year = 2021  # 변수에 __ 를 준다면 정보은닉의 의미가 된다.
        else:
            self.__year = year
    
    def getYear(self):
        return self.__year  # 즉, 캡슐화가 되어버린다. 외부에서 year라는 변수에 직접 접근이 불가능해진다


'''
public vs private
instance variable - public 변경 private? __instance variable
instance variable - public 변경 private? __instance function
'''

class HidingClass (object):

    def __init__(self, name, dept, num):
        self.utype = self.__class__.__name__    # __내장속성__
        self.name = name
        self.__dept = dept  # private 으로 변경 사용
        self.num  = num

    def getDept(self):
        return self.__dept  # 클래스 내에서는 접근이 가능하다

    def __getInfo(self):
        return "__로 시작했기 때문에 해당 함수는 외부에서 접근이 되지 않는다"

'''
다향성 
상위 클래스에 정의된 함수를  하위클래스에서 해당 함수를 재정의 (method overriding)
'''

# [실습]
# 1. Account class 작성 - account, balance, interestRate
# 2. accountInfo() - 계좌의 정보를 출력한다(account, balance, interestRate)
# 3. deposit(amount) - 계좌 잔액에 매개변수로 들어온 amount를 누적한다.
# 4. printInterestRate() - 현재 잔액에 이자율을 계산하여 소수점 자리 2자리까지 출력한다.
# 5. withDraw(amount) - 매개변수로 들어온 금액만큼을 출금하여 잔액을 변경한다.
# 단) 잔고가 부족할 경우 '잔액이 부족하여 출금할 수 없습니다' 출력한다.

class Account (object):
    def __init__(self, account, balance, interestRate):
        self.account = account
        self.balance = balance
        self.interestRate = interestRate

    def accountInfo(self):
        print('계좌번호 {}, 현재잔액{}'.format(self.account, self.balance))
    def deposit(self, amount):
        self.balance += amount
    def printInterestRate(self):
        print('%.2f' % (self.balance + self.balance * self.interestRate))
    def withDraw(self, amount):
        if self.balance < amount :
            print ("잔액이 부족하여 출금 할 수 없습니다")
        else:
            self.balance -= amount
