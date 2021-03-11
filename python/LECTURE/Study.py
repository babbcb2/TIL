
# 출력
value = 1234
print(value * 2)

a = 12
b = 34
print(a,b,sep=',',end='-->')

# 입력
age = input('몇살이세요?')
print(age)

price = input('가격을 입력하세요:')
num = input('갯수를 입력하세요:')
sum = int(price) * int(num)
print ('총액은',sum,'원 입니다')

price = int(input('가격을 입력하세요:'))
num = int(input('갯수를 입력하세요:'))
sum = price * num
print ('총액은',sum,'원 입니다')

print(2**100)

a = 0x1a
print(a)

member = ['손오공','삼장법사','저팔계','사오정']
for m in member:
    print(m, '출동')

a = 7%2
print(a)

age = int(input('너 몇살이니?'))
if age < 19:
    print ('애들은 가라')
print ('환영합니다')

a = 3
if a > 1 and a < 10 :
    print('ok')

student = 1
while student <= 5 :
    print (student,'번 학생의 성적을 처리한다')
    student += 1

num = 1

sum = 0
while num <= 100:
    sum += num
    num += 1
print("sum",sum)

for student in range(1,6):
    print(student,'번 학생의 성적을 처리한다')

for x in range (1, 51):
    if (x % 5 == 0):
        print('+', end='')
    else:
        print('-', end='')

score = [92,86,68,120,56]
for s in score:
    if (s < 0 or s > 100):
        break
    print(s)
print('성적처리 끝')

score = [92,86,68,-1,56]
for s in score:
    if (s == -1):
        continue
    print(s)
print('성적처리 끝')

for dan in range (2,100):
    print(dan, '단')
    for hang in range (2, 10):
        print(dan, '*', hang ,'=', dan * hang)
    print()

print('3 + 4 =?')
while True:
    a = int(input('정답을 입력하시오:'))
    if (a == 7) : break
print('참잘했어요')

s = "python programming"

print(len(s))
print(s.find('o'))
print(s.rfind('o'))
print(s.index('r'))
print(s.count('n'))

score = [88, 95, 70, 100, 99]
sum = 0
for s in score:
    sum += s
print('총점 :',sum)
print('평균 :', sum/len(score))

int(3.3)
int(5/2)
int('10')

float(5)

x = 15
if x >= 10:
    print('10이상입니다.')
    if x == 15:
        print('15 입니다')
    if x == 20:
        print('20 입니다다')

x = int(input())
if x == 10:
    print('10입니다.')
if x == 20:
    print('20입니다.')

x = int(input())
if x == 10:
    print('10입니다.')
else:
    print('10 아닙니다')

x = 11
y = 20
if x == 10 and y == 20 :
    print('참')
else:
    print("거짓")

writtenTest = 76
codingTest = True
if writtenTest > 75 and codingTest == True:
    print('합격')
else:
    print('탈락')

x = 30

if x == 10:
    print('10 입니다')
elif x == 20:
    print('20 입니다.')
else:
    print('10도 20도 아닙니다')

# 문제 1)
# 사용자로부터 하나의 값을 입력받아(input)
# 해당 값에 20을 뺀 값을 출력하라
# 단) 출력 값의 범위는 0 ~255이다
# 예를 들어 결과값이 0보다 작은 값이되는 경우 0을 출력하고
# 255보다 큰 값이 되는 경우 255을 출력해야한다.

num = int(input("enter your number"))
if num - 20 < 0 :
    print (0)
elif num - 20 > 255 :
    print(255)
else :
    print(num -20)

# 문제 2)
# 사용자로부터 입력 받은 시간이 정각인지 판별하라.
# 현재시간 : 02:00
# 현재시간 : 03:10

Strclock = '02:00', '03:10'
if Strclock == '02:00' :
    print(True)
else:
    print(False)

# 문제 3)
# 사용자로 입력받은 단어가 아래 fruit 리스트에 포함되어
# 있는지를 확인하라.
# 포함되었다면 "정답입니다"를 아닐 경우 "오답입니다" 출력하라.

User = input('enter your fruit?')
funit = ['사과','포도','딸기']

if User in funit:
    print ('정답입니다'.format(User))
else:
    print('오답니니다'.format(User))

# 사용자로부터 하나의 값을 입력받아(input)
# 해당 값에 20을 뺀 값을 출력하라
# 단) 출력 값의 범위는 0 ~255이다
# 예를 들어 결과값이 0보다 작은 값이되는 경우 0을 출력하고
# 255보다 큰 값이 되는 경우 255을 출력해야한다.

num = int(input('your number?'))

if num - 20 < 0 :
    print(0)
elif num > 255 :
    print(255)
else :
    print(num-20)

# 문제 4)
# 투자 경고 종목 리스트가 있을 때
# 사용자로부터 종목명을 입력 받은 후
# 해당 종목이 투자 경고 종목이라면 '투자 경고 종목입니다'를
# # 아니면 "투자 경고 종목이 아닙니다."를 출력하는 프로그램을 작성하라.


User = str(input('투자 종목은?'))
Helllist = ['삼성전자','씨젠']

if User in Helllist:
    print('투자 경고 종목입니다'.format(Helllist))
else:
    print('투자 경고 종목이 아닙니다.'.format(Helllist))

# 아래와 같이 fruit 딕셔너리가 정의되어 있다.
# 사용자가 입력한 값이 딕셔너리 키 (key) 값에 포함되었다면 "정답입니다"를
# 아닐 경우 "오답입니다" 출력하라.
fruit = {"봄" : "딸기", "여름" : "토마토", "가을" : "사과"}
userfruit = input("enter your fruit : ")
if userfruit in fruit :
    print("정답입니다.")
else:
    print("오답입니다.")

# 점수 구간에 해당하는 학점이 아래와 같이 정의되어 있다.
# 81~100 A
# 61~80	 B
# 41~60	 C
# 21~40	 D
# 0~20	 E
# 사용자로부터 score를 입력받아 학점을 출력하라

User = int(input("enter your score"))
if 100 => ser > 80 :
    print("A")
elif User > 60 :
    print("B")
elif User > 40 :
    print("C")
elif User > 20 :
    print("D")
else:
    print('F')

# 문제 8)
# 사용자로부터 세 개의 숫자를 입력 받은 후
# 가장 큰 숫자를 출력하라.
# input number1: 10
# input number2: 9
# input number3: 20

num = [10,9,20]
print(max(num))

# 문제 9)
# 휴대폰 번호 앞자리에 따라 통신사는 아래와 같이 구분된다. 사용자로부터 휴대전화 번호를 입력 받고, 통신사를 출력하는 프로그램을 작성하라.
# 번호	통신사
# 011	SKT
# 016	KT
# 019	LGU
# 010	알수없음
# 휴대전화 번호 입력: 011-345-1922

PhoneNum = str(input('enter your phone Number?'))
if PhoneNum == '011' :
    print('SKT 입니다')
elif PhoneNum == '016' :
    print('KT 입니다')
elif PhoneNum == '019' :
    print('LGT 입니다')
else:
    if PhoneNum == '010' :
        print('알수없음')

# 문제 10)
# 주민등록번호 뒷 자리 7자리 중 첫째 자리는 성별을 나타내는데
# 1, 3은 남자 2, 4는 여자를 의미한다.
# 사용자로부터 13자리의 주민등록번호를 입력 받은 후 성별 (남자, 여자)를 출력하는 프로그램을 작성하라.
# >> 주민등록번호: 821010-1635210

idCard = str(input('enter your ID card number?'))
if idCard[7] == str(1 or 3) :
    print('남자입니다')
else:
    if idCard[7] == str(2 or 4) :
    print('여자입니다')


# 문제 11)
# 주민등록번호의 뒷 자리 7자리 중 두번째와 세번째는 지역코드를 의미한다.
# 주민 등록 번호를 입력 받은 후 출생지가 서울인지 아닌지 판단하는 코드를 작성하라
# 지역코드	출생지
# 00 ~ 08	서울
# 09 ~ 12	부산

idCard = input('enter your ID card number?')
seoul = ['00','01','02','03','04','05','06','07','08']
busan = ['09','10','11','12']

if idCard[8:10] in seoul :
    print('Seoul 입니다'.format(idCard))
else:
    if idCard[8:10] in busan :
        print('Busan 입니다'.format(idCard))

# 문제 12)
# 어떤 대학교를 졸업하려면 적어도 140학점을 이수해야
# 하고 평점이 2.0은 되어야 한 다고 하자.
# 이것을 파이썬 프로그램으로 검사해보자.
# 사용자에게 이수학점수와 평점을 물어보고 졸업 가능 여부를 출력하는 프로그램을 작성해보자.

credits = float( input("이수한 학점을 입력하세요 : "))
avg = float( input("평점을 입력하세요 : "))
if credits >= 140 and avg >= 2 :
    print('졸업을 축하합니다')
else:
    print('졸업학점 미달입니다')

# 문제 13)
# 1부터 10사이의 난수를 생성하고 숫자를 맞춰보자

from random import randint
answer = randint(1,5)
print(answer)

# 문제 14)
# input()함수를 이용하여 입력받은 숫자가 홀수인지 짝수인지를 판단하는 프로그램을 작성하라.
# 홀수면 '홀수'라고 출력하고 짝수면 '짝수'라고 출력하시오
# +, - , / , * , %(나머지 연산자)

inputnumber = int(input("enter your digit : "))
if inputnumber%2 == 1 :
    print("홀수")
    pass
else :
    print("짝수")

print('hello wolrd')

print("안녕하세요.\n 만나서 \t\t 반갑습니다")

print ("오늘은", "일요일")

print('naver', 'kakao', 'sk', 'samsung', sep=';')

print('naver', 'kakao', 'sk', 'samsung', sep='/')

print("first", end="")
print("second")

samsung = 50000
sum = samsung * 10
print(sum)

s = "hello"
t = "python"
print(s + "!", t)

a = "132"
print (type(a))

num_str = "720"
print (type(int(num_str)))

num = 100
print(type(str(num)))

data = "15.79"
data2 = float(data)
print (data2, type(data2))

year = "2020"
print (int(year)-1)
print (int(year)-2)

air = 48584
card = 36
print (air * card)


lang = 'python'
print(lang[0], lang[2])

license_plate = "24가 2201"
print(license_plate[-4:])

string = "홀짝홀짝홀짝"
print (string[::2])

string_01 = "PYTHON"
print (string_01[::-1])

Phone_number = "010-1111-2222"
Phone_number = Phone_number.replace("-", " ")
print (Phone_number)