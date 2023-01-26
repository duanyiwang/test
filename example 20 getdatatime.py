import datetime

current_datatime = datetime.datetime.now()
print(current_datatime, type(current_datatime))

str_time = current_datatime.strftime("%Y年%m月%d日 %H:%M:%S")
print(str_time, type(str_time))

print(current_datatime.year)
print(current_datatime.month)
print(current_datatime.day)
print(current_datatime.hour)
print(current_datatime.minute)
print(current_datatime.second)



