# 변수 정의 및 생성
# 블럭단위 실행 단축키 (shift + art + e)

intvalue = 123
floatvalue = 3.14
boolvalue = True
strvalue = 'jslim'

print(type(intvalue),type(floatvalue),type(boolvalue),type(strvalue))


# type casting 
# 데이터의 형태를 변경
numStr = "720"
numNum = 100
print (int(numStr) + numNum)    # --> 820 출력 (숫자)
print (numStr + str(numNum))    # --> 720100 출력 (문자)

year = "2021"
print(int(year)-1)

# List
ListAry = ['python','Anaconda']
print(type(ListAry))

# dict
dictValue = {
    "name" : "machine learning",
    "version" : 2.0
}
print(type(dictValue))

# tuple()
tupleValue = (3,)
print(type(tupleValue))

# set {}
setValue = {3,5,7}
print(type(setValue))

# keyboard input
# function syntax
'''
접근지정자 리턴타입 함수명(매개변수) {
}
python
def 함수이름() : 
    statement

'''
# input()
inputNumber = input('숫자를 입력하세요:')
print(inputNumber)
print(type(inputNumber))

# 문자형(str)
str01 = 'I am Python'
str02 = "Python"
str03 = """this is a
multi
sample text"""

seqText = 'Talk is cheap. Show me the code'
print(seqText)

# dir
print( dir(seqText))

# slicing
print(seqText[3])
print(seqText[-1])
print(seqText[0:4])
print(seqText[-6:])
print(seqText[ : : -1])

# 아래 문자열에서 '홀'만 출력하세요~
string = '홀짝홀짝홀짝홀짝홀짝'
print(string[::2])

# 문자열 조작을 위한 많은 내장 함수를 제공하고 있다.
string = "python"
print("capitalize :", string.capitalize())

# 문자대체 replace (oldchar, newchar)
# 특정 문자열을 찾아 다른문자열로 바꾼다
phoneNumber = '010-1111-2222'
replacePhoneNumber = phoneNumber.replace('-',"")    # '-' > '" 으로 문자열 변경
print(replacePhoneNumber)

string = 'alsdjfasdf'
print(string.replace('a',"A"))

# 문자열 split()
# 구분자 기준으로 문자열을 분할한다

# 문제) 아래 문자열에서 도메인만 출력하고 싶다면?
url = "http://www.naver.com"
urlSplit = url.split('.')       # --> 구분자 '.' 기준으로 분리
print(urlSplit)                 # --> ['http://www', 'naver', 'com'] 출력
print('domain:',urlSplit[-1])   # --> domain: com 출력

# 문자열에서 공백 제거 함수 : strip(), rstrip(), lstrip()
# 대문자, 소문자 변환 함수 : upper(), lower()
companyName = '   samsung    '
print(companyName.strip(),len(companyName.strip()))
print(companyName.rstrip(),len(companyName.rstrip()))
print(companyName.lstrip(),len(companyName.lstrip()))
print(companyName.upper())

# endswitch()
# 특정문자열로 끝나는지 뒷부분만 비교
fileName = 'report.txt'
isExits = fileName.endswith(('xls', 'xlsx','csv'))
print(isExits, type(isExits))

# in, not in -> true : False
myStr = "This is a sample text"
print("sample" in myStr)

# 문자의 빈도 count()
# 문자 찾기 find()
# 문자의 인덱스 index()

brandName = 'cocacola'
print(len(brandName),brandName.count('c'),brandName.find('f'), brandName.index('a'))
# --> 8 3 -1 3 출력