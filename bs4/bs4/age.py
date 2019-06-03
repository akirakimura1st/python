from dateutil.relativedelta import *
import datetime

today = datetime.date.today()
year = int(input('西暦何年に生まれた？'))
month = int(input('何月生まれ？'))
day = int(input('何日？'))
born = datetime.date(year, month, day)

age = relativedelta(today, born)
print(age)