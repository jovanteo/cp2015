import calendar

x = 1
while x != 0:
    month = int(input("input month in integer form(i.e. 1-12): "))
    year = int(input("input year: "))

    print("There are", calendar.monthrange(year, month)[1], "days in", calendar.month_name[month], year)
