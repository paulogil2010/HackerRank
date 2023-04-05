"""You are given a date. Your task is to find what the day is on that date."""


import calendar


if __name__ == '__main__':
    inputed_date = input().split()  # MM DD YYYY

    date = calendar.weekday(
        year=int(inputed_date[2]),
        month=int(inputed_date[0]),
        day=int(inputed_date[1]),
    )
    print(calendar.day_name[date].upper())