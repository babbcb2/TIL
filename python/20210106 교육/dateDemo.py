
# python date type
from datetime import date, datetime
# 이거는 datetime 패키지에서 date와 datetime 모듈들을 가져오겠다. 라는 의미입니다.

today = date.today()
print('date -',type(today), today, today.year, today.month, today.day)
print('{} 년도, {} 월, {} 일'.format(today.year,today.month, today.day))

# 시간
todayDateTime = datetime.today()
print('datetime -', todayDateTime)
print('{} 시 , {} 분, {} 초'.format(todayDateTime.hour, todayDateTime.minute, todayDateTime.second))

# pip | conda install
# dateutil

from datetime import  date, timedelta
from dateutil.relativedelta import relativedelta

today = date.today()
days = timedelta(days=-1)
print('오늘 이전 하루 - {}'.format(today+days))

# year, month 관련된 옵션을 필요로 하신다면
# relativedelta

months = relativedelta(months=-2)
print('두달 전 오늘 - {}'.format(today+months))

from dateutil.parser import parse

userDate = parse("2021-06-04")
print('parse date -', userDate)

userDate = datetime(2021, 12, 25)
print('datetime -', userDate, type(userDate))

# 날짜 객체의 출력형식을 원하는 것으로 변경
today = datetime.today()

# 날짜형식 -> 문자열 형식의 포맷으로 지정
# strftime()
print("{}".format(today.strftime('%m-%d-%y')))

# 문자열형식 -> 날짜형식 (strptime)

strDate = '2021,01,06-11:12:40'
userDate = datetime.strptime(strDate,'%Y,%m,%d-%H:%M:%S')
print(type(userDate),userDate)




