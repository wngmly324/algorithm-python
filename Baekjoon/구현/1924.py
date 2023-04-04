import calendar

x, y = map(int, input().split())
daylist = ['MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT', 'SUN']

def findDay(x, y):
    theDay = calendar.weekday(2007, x, y)
    return daylist[theDay]

print(findDay(x, y))

###################################################################

day = 0
month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
week = ['MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT', 'SUN']

x, y = map(int, input().split())

for i in range(x-1):
    day += month[i]

day = (day + y) % 7

print(week[day])