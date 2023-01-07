# import time
#
# print("the epoch of this system starts at " + time.strftime('%c', time.gmtime(0)))
#
# print("The current timezone is {0} with an offset at {1}".format(time.tzname[0], time.timezone))
#
# if time.daylight != 0:
#     print("Daylight saving time is in effect for this location")
#     print("The DZT timezone is " + time.tzname[1])
#
# print("Local time is " + time.strftime('%Y-%m-%d %H:%M:%S', time.localtime()))
# print("UTC time is " + time.strftime('%Y-%m-%d %H:%M:%S', time.gmtime()))


import datetime

print(datetime.datetime.today())
print(datetime.datetime.now())
print(datetime.datetime.utcnow())
