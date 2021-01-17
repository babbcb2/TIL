from ai.oop.Day6__OOP_inheritance import *
car01 = Car ('GV70', 4, 2400)
car01.carInfo()

# parent = Parent('부모','공무원')
# print('parent -',parent.display())

# child01 = Child01('자식','강사',49)
# rint (child01.display())

# stu01 = StudenVO('임정섭',49,'seoul','1992')
# print('stu info -', stu01.stuInfo())
#
# tea01 = TeacherVO('섭섭해',4,'busan','python')
# print('stu info -', tea01.teaInfo())
#
# emp01 = ManagerVO('장호연',29,'seoul','HRD')
# print('emp info -', emp01.empInfo())

# userDate = MyDate()
# # userDate.year = -2021
# userDate.setYear(-2021)
# print(userDate.getYear())

hiding = HidingClass('창호','교육팀',100)
print('utype -', hiding.utype)
print('name -', hiding.name)
#print('dept -', hiding.__dept)
print('num -', hiding.num)
print('call getDept -', hiding.getDept())
print('call __getInfo -', hiding.__getInfo())

# 다향성
stu01 = StudenVO('임정섭',49,'seoul','1992')
tea01 = TeacherVO('섭섭해',4,'busan','python')
emp01 = ManagerVO('장호연',29,'seoul','HRD')

perList = []
perList.append(stu01)
perList.append(tea01)
perList.append(emp01)
print(perList)

for obj in perList:
    print(obj.perInfo())
    # if isinstance(obj, studentVO):
    #     print(obj.stuInfo())
    # elif isinstance(obj, TeacherVO):
    #     print(obj.teaInfo())
    # else:
    #     print(obj.empInfo())


account = FundAccount('444-2919-1234', 500000, 0.073)

account.accountInfo()
account.withDraw(600000)
account.deposit(200000)
account.accountInfo()
account.withDraw(600000)
account.accountInfo()
print('현재 잔액의 이자를 포함한 금액')
account.printInterestRate()