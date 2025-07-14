# Working with Dates and Time

'''
The datetime Module

datetime.date
datetime.timedelta
datetime.datetime
'''
# import datetime

# datetime.date
'''
print(datetime.date(2025, 1,18))

d = datetime.date(2025,1,18)
print(d)
print(d.year)
print(d.day)
print(d.month)
d = datetime.date.today()
print(d)
'''

'''
# datetime.datetime
d = datetime.datetime(2025,1,18)
print(d)
d = datetime.datetime(2025,1,18,12,30,10)
print(d)
print(d.year)
print(d.second)
print(d.hour)
'''
'''
# datetime.timedelta
now  = datetime.datetime.now()
datetime.datetime(2014,3,5,18,13,51,230000)
then = datetime.datetime(2014,2,16)
delta = now - then
print(type(delta))
print(delta.days)
'''

# The time Module
import time

'''
print(time.gmtime(0))

time.ctime
time.sleep
time.strftime
time.time
'''

'''
# time.ctime
print(time.ctime())

for x in range(5):
    time.sleep(2)
    print("Sleep for 2 seconds")
'''

# time.strftime
print(time.strftime("%Y-%m-%d-%H.%M.%S", time.localtime()))

# time.time
print(time.time())