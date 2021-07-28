# Python Program to Convert String to Datetime

from datetime import datetime

string_datetime = "20-07-2021 17:14:00"
format_datetime = "%d-%m-%Y %H:%M:%S"
datetime_object = datetime.strptime(string_datetime, format_datetime)
print(datetime_object)
