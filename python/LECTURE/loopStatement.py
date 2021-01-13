
# python control statement for looping
# for ~ in range(start index, end index, step)
# for ~ in list, dict

userSum = 0
for tmp in range(1, 11) :
    # print(tmp, end="\t")
    print(tmp)
    userSum += tmp
print('누적값은 : {} 입니다.'.format(userSum))

#userlist = [1,2,3,4,5]
userlist = [(1,2),(3,4),(5,6)]
for tmp01, tmp02 in userlist :
    print(tmp01, tmp02)  # 튜플 형태로 받고 있다.
    userSum += tmp01 + tmp02
print()
print('누적값은 : {} 입니다.'.format(userSum))

userDict = {'name' : 'jslim', 'gender':'m'}
for (key, value) in userDict.items():
    print("{},{}".format(key,value))

scores = [100, 50, 80, 90, 70, 60]
for idx in range(len(scores)) :
    userSum += scores[idx]

print('scores 합 %d ' % userSum)

# %d, %s, %f
print ('scores 합 %d' % userSum)

# list Comprehension
'''
[ for 구문을 통한 반복적인 표현식을 이용할 수 있다 if ]
'''
userlist = [1,2,3,4,5,6,7,8,9]
userList02 = [tmp ** 2 for tmp in userlist]
print('compregension -', userList02)
userlist03 = [tmp **2 for tmp in userlist if tmp % 2 == 0]
print('compregension if-', userlist03)

# dict 에서도 사용 가능
userDict = { 'Test' + str(tmp) : tmp ** 2 for tmp in range(1,10) }
print(userDict)
