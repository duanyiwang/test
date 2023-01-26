import datetime

birthday = "1987-02-10"
birthday_date = datetime.datetime.strptime(birthday, "%Y-%m-%d")
print(birthday_date, type(birthday_date))
current_date=datetime.datetime.now()

date= current_date-birthday_date
print(date.days/365,type(date))