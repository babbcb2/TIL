a = 123
b = 3.14
c = 3.14E10

print(type(a))
print(type(b))
print(type(c))

div = 3/4
print (div)

rsult = 3 ** 3
print(rsult)

rsult = 10 % 3
print(rsult)

rsult = 10 // 3
print(rsult)

# sequence - list
# 임이의 객체를 순서대로 저장하는 집합 자료형
# 보편적으로 사용하는 방법
a = []
print (type(a))
a = list()
print (type(a))
a = [1,2,3]
print (a)

#indexing
print (a[0])
print (a[1])
print (a[2])
print (a[-1])

# slicing
print(a[0:2])

a = [1, 2, 'hello', 3.14]
a = [1, 2, ['show','me','the','money'], 3.14]
print(type(a[2]))
print(a[2][2:])

a = [1,2,3]
b = [4,5,6]
print(a+b)
print(a*3)

print('p','y','t','h','o','n')
print('p','y','t','h','o','n', sep="")
print('p','y','t','h','o','n', sep="-")

#end 옵션
print ('welcome to ', end="")
print ('IT News')

#format 사용법(d, s, f)


# tuple
# ()
a = ()
print(type(a))

# type casting
a = list(a)
print( type(a))