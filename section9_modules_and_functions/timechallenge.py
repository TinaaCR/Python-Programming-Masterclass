import pytz
import datetime

print(list(pytz.common_timezones))


while True:
    country = input("choose a timezone: ")
    if country == '0':
        break
    tz_to_display = pytz.timezone(country)

    local_time = datetime.datetime.now(tz = tz_to_display)
    print("The time in {} is {}".format(country, local_time))
    print("UTC is {}".format(datetime.datetime.utcnow()))



