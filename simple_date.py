from datetime import datetime as dt
from dateutil.parser import parse

now = '2018-11-1820:36:02.819000'
now1 = now.strftime("%Y-%m-%d-%H.%M.%S")
print(now1)
#strftime("%Y-%m-%d-%H.%M.%S")
#get_date_obj = parse("2012-11-01T04:16:13-04:00")
get_date_obj = parse(now)
#print(dt.fromtimestamp(now).strftime("%Y-%m-%d"))
print(get_date_obj.strftime("%Y-%m-%d"))
print(type(get_date_obj))
