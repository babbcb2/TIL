
'''
palindrom (회문)
단어를 거꾸로 읽어도 제대로 읽는 것과 같은 단어 또는 문장
level, sos, rotator, 'nureses run'
기준이 필요(중앙을 기준으로해서 첫글자와 마지막 글자를 비교)
반복문
// - 목ㅆ을 취하는 연산자
'''
str = 'jslim9413'
idx = len(str) // 2
print(str[idx])

def isPalindrom():
    isFlag = True
    word = input('회문검사를 위한 단어를 입력하세요 >>> ')
    for idx in range(len(word) // 2):
        if word[idx] != word[-1 - idx] :
            isFlag = False
            break
    return isFlag

def reversedPalindrom():
    word = input('회문검사를 위한 단어를 입력하세요 >>> ')
    print(word == word[::-1])

# palindrom words.txt 파일의 단어를 읽어서 회문인 단어만 출력

def pickleReader():
    with open(file='./word/palindrome_words.txt', mode='r') as file :
        for line in file:
            line = line.strip('\n')
            if line == line[::-1]:
                print(line)

# 문자열에서 n개의 연속된 요소를 추출한다면?
# 자연어처리
# hello -> he/el/ll/lo

text = "hello"
for idx in range(len(text)-1):
    print(text[idx], text[idx+1], sep='')

text = 'this is python script'
textlist = text.split()
print(type(textlist),textlist)

for idx in range(len(textlist)-1):
    print(textlist[idx], textlist[idx+1], sep='')

# zip ()
num  = [  1,     2,    3,     4]
name = ['hong','gil','dong','guy']

dic = {}
for key, value in zip(num, name):
    dic[key] = value
print(dic)

'''
input 함수를 이용해서 문자열을 입력받고
예시) python is a programming language that lets your work quickly
input 함수를 이용해서 gram 할 숫자를 입력 받고
예시) n개
입력된 숫자에 해당하는 단어 N-gram 튜플형식으로 출력
주의) 입력된 문자열의 단어갯수가 입력된 정수 미만이라면 예외를 발생
'''

def zipNgram ():
    sentences = input('sentences :')
    gram      = int(input('gram :'))
    words = sentences.split()

    # for idx in range(len(words)-gram+1):
    #     print(words[idx:idx+gram])

    ngram = zip(*[words[idx:] for idx in range(gram)])
    for idx in ngram:
        print(idx)

zipNgram()


