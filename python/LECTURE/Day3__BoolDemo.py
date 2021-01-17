# python bool 타입의 특징
# bool
# True(T), False(F)
# not, and, or -> 논리연산
# & , |, ~ -> 비교연산
## Fasle 로 간주되는 상황
## "", [], (), {}, 숫자(0이외의 숫자는 True), None

xValue = 5  # 0101
yValue = 0  # 0000  -> 0000 -> 0
            #       -> 0101 -> 5

print(xValue & yValue)      # 0101 & 0000 -> 0
print(bool(xValue&yValue))
print(xValue | yValue)
print(bool(xValue | yValue))

trueValue = True
falseValue = False
print(int(trueValue), trueValue)    # --> 1 True 출력
print(int(falseValue), falseValue)  # --> 0 False 출력

print(trueValue & falseValue)
print(trueValue | falseValue)

print ('and - ' , trueValue and falseValue)
print ('or - ' , trueValue or falseValue)
print ('not - ' , not trueValue)