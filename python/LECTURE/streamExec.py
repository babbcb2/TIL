
'''
a.py  b.by
    ----
    (has a~)
class A
    | (is a ~)
class B(A)
class A ---- class B

binary 형식의 입출력
- 객체직렬화(Serializable) -> 파일저장
- pickle
010111010
'''

scores = {'kor':90, 'eng':95, 'math':70, 'scien':82}
print(type(scores))

# scores 객체 정보를 xxx.txt 파일로 저장
def pickleWriter():
    with open(file='dict.txt', mode='w', encoding='utf-8') as file :
        for (key, value) in scores.items():
            file.write('{}, {}\n'.format(key, value))
    print('저장완료!!')
pickleWriter()

import pickle
def pickleWriter02():
    with open(file='dictPickle.txt', mode='wb') as file :
        pickle.dump(scores, file)
    print('객체 직렬화를 통한 파일 저장')
pickleWriter02()

# 파일 읽어 들일떄
def pickleReader():
    with open(file='dictPickle.txt', mode='rb') as file :
        dictScores = pickle.load(file)
        print('파일로딩 -', dictScores, type(dictScores))
    print('객체 직렬화를 통한 파일 저장')
pickleReader()

'''
단어가 줄 단위로 저장된 cnt_words.txt 파일에서 10자이하인 단어의 갯수를 카운트하는
함수를 구현하고 호출 한다면
'''
def wordCntFunc():
    wordList = []
    with open(file='./word/cnt_words.txt', mode='r', encoding='utf-8') as file :
        for word in file.readlines():
            word = word.strip('\n')   # strip 을 써서 \n 줄바뀜 개행을 제거
            if len(word) <= 10:
                wordList.append(word)
    print('10자 이하의 단어의 갯수는 {}개 입니다.'.format(len(wordList)))
    print(wordList)
wordCntFunc()
#

pickleReader
'''
special_word.txt 파일에서
문자가 'c'가 포함된 단어를 출력하는 함수를 만들어서 호출한다면?
주의) 단어를 출력할 때는 등장한 순서대로 출력하며 ,. 은 출력하지 않는다
'''

def wordSpecialFunc():
    with open(file='./word/special_words.txt', mode='r', encoding='utf-8') as file :
        words = (file.read().split())
        print(words,type(words))
        for word in words :
            if 'c' in word:
                print(word.strip(',.'))
wordSpecialFunc()

'''
zipcode.txt
input () 이용해서 동 이름을 입력받아
입력예시) 개포
해당하는 동의 주소를 출력하는 함수를 정의하고 호출한다면?
- startswith(), endwith()
'''

def searchAddfcun():
    dong = input('찾는 동을 입력하세요 :')
    with open(file='./word/zipcode.txt', mode='r', encoding='utf-8') as file :
        line = file.readline()
        print(line, type(line))
        while line :
            address = line.split('\t')
            if address[3].startswith(dong) and address[3].endswith('동'):
                print('['+address[0]+']',address[1], address[2], address[3], address[4], address[5])
            line = file.readline()
searchAddfcun()

'''
csv, excel 파일은 -> pandas lib 사용
- pip install pandas
- conda install pandas
- service_bim.csv
'''

import pandas as pd
bmiDataset = pd.read_csv('./word/service_bmi.csv', encoding='utf-8')

print(bmiDataset.info())
print(bmiDataset.head())
print(bmiDataset.tail())

# 속성에 대한 접근 - Series
print(bmiDataset.height, type(bmiDataset.height))
print(bmiDataset['weight'])
print(bmiDataset['label'])

# 키/몸무게 평균
print('키 agv {}, 몸무게 avg {}'.format(sum(bmiDataset.height)/len(bmiDataset.height),
                                       sum(bmiDataset['weight'])/len(bmiDataset['weight'])))

# 키 최대 / 몸무게 최대
print('max height -', max(bmiDataset.height))
print('max weight -', max(bmiDataset.weight))

# label 빈도수
labalCnt = {}
for label in bmiDataset['label'] :
    labalCnt[label] = labalCnt.get(label, 0) + 1
print(labalCnt)

'''
spam_data.csv
'''

spamDataset = pd.read_csv('./word/spam_data.csv', header=None, encoding='ms949')
print(spamDataset.info())
print(spamDataset.head())

targer = spamDataset[0]
print('targer -',targer, type(targer))
text = spamDataset[1]
print('text -',text, type(text))

# spam = 1, ham - 0 새로운 타켓을 만들고 싶다면?
targer = [ 1 if t == 'spam' else 0 for t in targer]
print(targer)

# 코드클린 - 문자열에 대한 정규표현식을 이용해서 문자를 제거하는 작업
# 정규표현식
# import re (레귤러 익스프레션)
'''
1. 메타문자
. ^ $ * + ? {} [] \ | ()
. -> 무엇이든 한글자를 의미
^ -> 시작문자 지정
* -> 0 or more
+ -> 1 or moer
? -> 0 or 1
예)
[abc] -> a,b,c 한문자와 매치
[^0-5] -> 반대의 매칭의 결과 출력
^[0-5] -> 0-5 로 시작하는 매칭 결과 출력

문자클래스
\d -> 숫자의 자릿수
\D -> 숫자가 아닌 문자매칭의 자릿수
\w -> 문자+숫자
\w -> 문자+숫자 아닌 문자와 매치
\s -> 공백
010-0000-0000
^\d{3}-\d{4}-\d{4}

- sub()
- match()
- search()
- findall()
- finditer()
'''

import re
p = re.compile('[a-z]+')
match = p.match('python')
print(match)

# 텍스트 전처리 - (특수문자, 숫자, 공백, 영문제거) => 한글 단어만 추출
text = spamDataset[1]
print(text)
def cleanText(str):
    str = re.sub('[,.?!:;]', ' ', str)
    str = re.sub('[0-9a-zA-Z]',' ',str)
    str = ' '.join(str.split())
    return str

cleanData = [ cleanText(t) for t in text ]
print(cleanData)

# xls 파일
kospiDataset = pd.ExcelFile('./word/sam_kospi.xlsx')
kospi = kospiDataset.parse('sam_kospi')
print(kospi.info())

from statistics import *
print('high mean', mean(kospi.High))

# json 파일 입출력
'''
json file : 네트워크 상에서 표준으로 사용되는 파일형식
구성 : {key : value, key : value}
encoding : python(dict,list)  -> json 문자열 (json file)   : dumps()
decoding : json 문자열         -> python (dict,list)       : loads()
import json     
'''

# python -> json
import  json
user = {'id':1234, 'name':'섭섭해'}
print(type(user))

jsonStr = json.dumps(user) # object -> json str
print(jsonStr,type(jsonStr))

# decoding
pyObj = json.loads(jsonStr)
print(pyObj, type(pyObj))
print(pyObj['name'])

'''
usagov_bitly.txt
'''
with open(file='./word/usagov_bitly.txt', mode='r', encoding='utf-8') as file:
    lines = file.readlines()
    rows = [ json.loads(line) for line in lines]
    for row in rows:
        for key, value in row.items():
            print('key - {}, value - {}'.format(key,value))
    # rows -> pd.DataFrame (행렬)
    rowsDF = pd.DataFrame(rows)

print(rowsDF.head)