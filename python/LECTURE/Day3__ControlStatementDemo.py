# control statemnet
# if(조건문), for(반복문), while(반복문)

# 사용자 입력 함수
# input()

name = input("Enter your Name :")
grade = input("Enter your Graed :")
company = input("Enter your Company :")
print(name, grade, company)

inputNumber = int(input("Enter your digit(1~100) :"))
# print(inputNumber%2 == 0)
if inputNumber%2 == 0 :     # input값에서 2를 나누고 몫이 0 일 경우
    print('짝수입니다.')
else:                       # input값에서 2를 나누고 몫이 0 아닐 경우
    print('홀수입니다.')

# 짝수인지 홀수인지를 판별?
# if, if ~ else, if ~ elif ~ else
# bool Ture / False

'''
other)
if(조건식) {
    true
}
else {
    false
}

python)
if True : 참이라면~ 
'''

# 값이 3의 배수인지 5의 배수인지 판별하고 싶다면?
number = int(input('Enter your number?'))
if (number%3 == 0 & number%5 == 0):
    print('{}은 3과 5의 배수입니다.'.format((number)))
else:
    print('{}은 3과 5의 배수가 아닙니다.'.format((number)))

# if ~ elif
if number%3 == 0:
    print('{}은 3의 배수입니다'.format(number))
elif number%5 == 0:
    print('{}은 5의 배수입니다'.format(number))
else:
    print('{}은 3과 5의 배수가 아닙니다'.format(number))


# 윤년의 조건
# 4의 배수이고, 100의 배수가 아니거나
# 400의 배수일 때를 윤년으로 본다면
# if 구문을 사용하여 년도와 월을 입력받아서 월의 마지막 일을 출력한다면?

year = 2020
if year%4 == 0 and year%100 != 0 or year%400 == 0 :
    print('{}는 윤년입니다'.format(year))
else:
    print('{}는 윤년이 아닙니다'.format(year))


# 윤년 체크 / 윤년이라면 마지막 2월의 마지막일을 체크
year = int(input('년도를 입력하세요 :'))
month = int(input('달을 입력하세요 :'))

year_month      = [31,28,31,30,31,30,31,31,30,31,30,31]
leap_year_month = [31,29,31,30,31,30,31,31,30,31,30,31]

if year%4 == 0 and year%100 != 0 :
    print('{}년, {}월의 마지막 일은 {} 입니다'.format(year, month, leap_year_month[month-1]))
elif year%400 == 0:
    print('{}년, {}월의 마지막 일은 {} 입니다'.format(year, month, leap_year_month[month-1]))
else:
    print('{}년, {}월의 마지막 일은 {} 입니다'.format(year, month, year_month[month-1]))

# if ~ in
Area = ['서울','부산','광주','제주']
region = '수원'
if region in Area :
    pass
else:
    print('{}지역은 포함하지 않습니다'.format(region)

AreaKeyDict = {'서울':100, '광주':200}
region = '부산'
if region in AreaKeyDict :
    pass
else:
    print ('{}값이 존재 하지 않습니다'.format(region))


# 삼항 연산자
num      = 9
result   = 0
result = num * 2    if  num > 5    else num + 2
print('삼항 연산자',result)
# num 값이 5보다 클경우 num * 2 출력하고, 아닐경우 num + 2 를 출력


# 문제 1)
# 사용자로부터 하나의 값을 입력받아(input)
# 해당 값에 20을 뺀 값을 출력하라
# 단) 출력 값의 범위는 0 ~255이다
# 예를 들어 결과값이 0보다 작은 값이되는 경우 0을 출력하고
# 255보다 큰 값이 되는 경우 255을 출력해야한다.


num01 = int(input('Enter your number'))
range01 = range(0,256)
if num01 > 255:
    print('255')
elif num01 < 0:
    print('0')
else:
    print(num01-20)

'''
# & == and
# & 비교연산, bitwise
# and 논리연산, Ture | False 연산)
-> x and y 있을 때 x 가 False x 값을 반홥하고
-> x 가 True y 값을 반환합니다.
'''