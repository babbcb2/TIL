# python control statement for looping
# for ~ in range(start index, end index, step)
# for ~ in list, dict

userSum = 0
for tmp in range(1, 11) :
    print(tmp, end="\t")    # -->  \t = 한줄로 출력
    userSum += tmp          # -->  1~10 값의 loop 돌면서 더해라
print('누적값은 : {} 입니다.'.format(userSum))     # -> 누적값은 : 110 입니다.


userlist = [1,2,3,4,5]
for tmp in userlist :
    print(tmp , end='\t')
    userSum += tmp
print('누적 값은 : {} 입니다.'.format(userSum))


userDict = {'name' : 'jslim', 'gender':'m'}
for (key, value) in userDict.items():
    print("{},{}".format(key,value))


scores = [100, 50, 80, 90, 70, 60]
for scores in scores :
    print(scores,end='\t')

for idx in range(len(scores)) :
    usersum += scores[idx]
print('scores 합 %d'% usersum)
# --> TypeError: object of type 'int' has no len()


# list Comprehension
'''
[ for 구문을 통한 반복적인 표현식을 이용할 수 있다 if ]
'''
userlist = [1,2,3,4,5,6,7,8,9]
userList02 = [tmp ** 2 for tmp in userlist]
print('compregension -', userList02)        # --> [1, 4, 9, 16, 25, 36, 49, 64, 81] 출력
userlist03 = [tmp **2 for tmp in userlist if tmp % 2 == 0]
print('compregension if-', userlist03)      # --> [4, 16, 36, 64] 출력


# dict 에서도 사용 가능
userDict = { 'Test' + str(tmp) : tmp ** 2 for tmp in range(1,10) }
print(userDict)


# 단어의 빈도수 구하기
# get() : 해당 key의 value 값을 가져옴
wordvec = ['love', 'word', 'cat', 'love', 'love']
print(len(wordvec))
wordcnt = {}               # wordcnt 를 dic 형태로 받겠다
for word in wordvec:       # wordvec 횟수만큼 word를 반복하겠다
    wordcnt[word] = wordcnt.get(word,0)+1
    print(wordcnt[word])
    print(wordcnt)

wordcnt02 = {}
for word in wordvec:
    if word in wordcnt02:
        wordcnt02[word] = 1
    else:
        wordcnt02[word] = 1

# [list], (tuple), {set}, dict{key,value)
# 1 ~~ 1000 sum
rangeSum = 0
for value in range(1,1001):
    rangeSum += value
    print('1~1000 의합은 {} 입니다'.format(rangeSum))

# 2000 ~ 2050 까지 올림픽 개최년도 출력
# 한줄에 5개의 년도출력 개행
cnt = 0                             # --> cnt 값으 0 으로 초기화
for year in range(2000,2051,4):     # --> 2000~2050년까지 4 step 씩 출력
    print(year, end='\t')           # year 출력시 행변경 없이 한줄로 출력
    cnt += 1                        # --> 반복을 할때맏 cnt 값이 +1 증가
    if cnt %5 == 0 :                # --> cnt 값이 5가 되어 반복 5번이 되면 한줄출력후 다음 loop 시작
        print()

# 세글자 이상의 단어만 출력
wordlist = ['i','am','study','python','laguage','!']
for word in wordlist:
    if len(word) > 3:
        print(word)

# isupper  -  대문자 확인
wordlist = ['i','am','study','PYTHON','laguage','IF','FOR']
for word in wordlist :
    if word.isupper() :     # wordlist 에 대문자를 확인하여 출력하라
        print(word)         # PYTHON, IF, FOR

# capitalize  -  첫번째 문자가 대문자가 된다
wordlist = ['dog','cat','pig','carrot','horse','!']
for word in wordlist :
    print(word.capitalize(), end='\t')
#   print( Dog Cat Pig Carrot Horse	! )

# upper  -  모든 문자를 대문자로
dumy = ['alkjfhlauhfwljaflAUHDO']
for w in dumy :
    if w.isupper() :
        print(w, end='')
    else :
        print(w.upper(), end='')

# 거꾸로 출력
wordlist = ['가','나','다','라']
for word in wordlist[::-1] :
    print(word)


# Break : 특정조건을 찾고 루프를 멈춤
# Continue : 특정조건을 만족했을때 제외하고 계속 루핑
search = 17
numbers = [14,3,4,7,10,24,17,2,33,34,36,57]
for num in numbers:
    if num == search:
        print('found -', num)
        break
    else:
        print('not found -', num)

for i in range(1,6):
    for j in range(1,4):
        print('i - {}, j - {}'.format(i,j))
'''
i - 1, j - 1
i - 1, j - 2
     ::
i - 5, j - 2
i - 5, j - 3
'''

# for ~ else
search = 5
numbers = [14,3,4,7,10,24,17,2,33,34,36,57]

for num in numbers :
    if num == search :
        print('found - ' , num)
        break
else :
    print('not found - ' , search)


# 구구단 만들기
for i in range(2, 10) :
    for j in range(1, 10) :
        print('{} * {} = {}'.format(i, j, ((i*j)), end='\t'))
     print()
    if i == 9 :
        break

# append():마지막 인덱스에 추가
# insert():특정인덱스에 추가
# extend():리스트의 요소추가
string ='''저는 여러분들과 함게 파이썬 강의중인 창호 입니다.
어려운 시기에 함께 되어서 반갑습니다!
얼른 오프라인으로 보고싶네요.'''
sentences = []
words = []
for s in string.split('\n') :   # string 을 split 으로 쪼개서 list 에 넣는다
    sentences.append(s)
    for w in s.split() :        # s 를 split 으로 쪼개서 list 에 넣는다
        words.append(w)
print(sentences , len(sentences))
print(words , len(words))


# 분류정확도
answer = [1,0,2,1,0]
predict = [1,0,2,0,0]
acc = 0
for idx in range(len(answer)) :
    fit = answer[idx] == predict[idx]
    #print (int(fit , end='\t'))
    acc += int(fit) * 20
print(acc)


# enumerate : 반복문 사용시 몇번째 반복문인지 확인이 필요하다면 인덱스번호, 컬렉션요소 확인 가능
booklist = ['sql','r','textmining','python','django','nlp']
for idx , book in enumerate(booklist) :
    print('index = {} , value = {}'.format(idx, book))


# while <expression> - 증감식
cnt = 5
while cnt > 0:
    cnt = cnt - 1
    print(cnt)

# list - pop () : 마지막 인덱스부터 빼면서 제거
whilelst = ['foo', 'bar', 'baz']
while whilelst:
    print(whilelst.pop())
print('while end')


# 난수를 발생시켜 횟수내 맞추는 게임
import random
ran = random.random()   # 0 ~ 1 사이의 난수를 발생시키는 실수형
print(ran)

ran = random.randint(0, 2) #정수형
print(ran)


#숫자범위 : 1-10 / 내가 입력한 숫자 > 난수 / 내가 입력한 숫자 < 난수
randnum = random.randint(1,10)
while True:
    userSum = int(input("Enter your number?"))
    if randnum == userSum :
        print('Success')
        break
    elif randnum > userSum :
        print('more')
    else:
        print('less')

# 1-100사이의 난수 , 도전횟수 20회 제한 , 출력결과:정답시도횟수,정답
randnum = random.randint(1, 100)
tries = 1
while tries <= 20 :
    usernum = int(input("숫자입력 : "))
    if randnum == usernum :
        print("정답")
        break
    elif randnum > usernum :
        print("업!!")
    else:
        print("다운!!")
    tries += 1
if usernum == randnum :
    print("정답 시도횟수{}".format(tries))
    print("정답{}".format(randnum))
else :
    print("정답{}".format(randnum))


# random.choices()
# 모집단 dataset에서 k개의 데이터를 샘플링
dataset = list(range(1,1001))
train = random.choices(dataset, k=10)
print(train)