import datetime


def get_diff_day(pdate, days):
    pdate_obj = datetime.datetime.strptime(pdate, "%Y-%m-%d")
    time_gap = datetime.timedelta(days=days)
    pdate_result = pdate_obj - time_gap
    return pdate_result.strftime("%y-%m-%d")


def get_delay_day(pdate, days):
    pdate_obj = datetime.datetime.strptime(pdate, "%Y-%m-%d")
    time_gap = datetime.timedelta(days=days)
    pdate_result = pdate_obj + time_gap
    return pdate_result.strftime("%y-%m-%d")


def get_all_day(start, end):
    date_list = []
    while start <= end:
        date_list.append(start)
        # start_ojb = datetime.datetime.strptime(start, "%Y-%m-%s")
        start_ojb = datetime.datetime.strptime(start, "%Y-%m-%d")
        day1_time = datetime.timedelta(days=1)
        start = (start_ojb + day1_time).strftime("%Y-%m-%d")
    return date_list


# print(get_diff_day("2023-01-20", 1))
# print(get_diff_day("2023-01-20", 3))
# print(get_diff_day("2023-01-20", 4))
# print(get_diff_day("2023-01-20", 7))
# print(get_delay_day("2023-01-20", 12))
# print(get_all_day("2022-12-20", "2023-01-05"))
start = "2022-12-20"
end = "2023-01-05"
datelist = get_all_day(start, end)
print(datelist)
