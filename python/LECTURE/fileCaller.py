
from ai.file.fileProc import *
# single line text inout
fileStream('file/hello.txt','w')

# multi line text inout
withMultiWriter('multiline.txt')
print('end')

lines = ['안녕하세요',
         '혹시 졸리우시면 ㅇㅇㅅㅋㄹ 콜?'
         '그럼 졸지말고 집중',
         '강사의 주옥같은 말을 한귀로 흘리면 안돼요']
withListFileWriter('listline.txt', lines)

# multi line text read
withListFileRead ('listline.txt', 'r')
