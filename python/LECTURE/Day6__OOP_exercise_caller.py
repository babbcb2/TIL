from ai.oop.Day6__OOP_exercise import *

# Marin 생성
marine01 = Marine(10, 100, 0, 0)
marine02 = Marine(10, 100, 0, 0)
marine03 = Marine(10, 100, 0, 0)
marine04 = Marine(10, 100, 0, 0)

# Medic 생성
Medic01 = Medic(0,100,0)
Medic02 = Medic(0,100,0)

# 병력을 list
troopList = []
troopList.append(marine01)
troopList.append(marine02)
troopList.append(marine03)
troopList.append(marine04)
troopList.append(Medic01)
troopList.append(Medic02)

# 기본정보 출력
for obj in troopList :
    obj.unitInfo()
    print("*"*50)

# Dropship 생성
ship = DropShip (0, 50, 0)

# 부대원을 태운다면?
ship.board(troopList)

# 공격목표지점으로 이동?
ship.attack()

# 부대원을 내린다면?
troopAttckList = ship.drop()

# 공격
for unit in troopAttckList:
    if isinstance(unit, Marine):
        unit.stimpack()
    unit.attack()


# unit = Unit(10,100)
# Unit.unitInfo()
# if unit.utype == 'unit':
#     print(True)
# else