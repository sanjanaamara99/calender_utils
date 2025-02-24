def yearly_calendar(year):
    """
    Prints the calendar for the given year.
    """
    initial_year = 1900
    initial_day = 1
    total_days = 0

    for i in range(initial_year, year):
        if (i % 4 == 0 and i % 100 != 0) or (i % 400 == 0):
            total_days += 366
        else:
            total_days += 365

    start_day = (initial_day + total_days) % 7

    months = ["January", "February", "March", "April", "May", "June",
              "July", "August", "September", "October", "November", "December"]

    weekdays = ["Su", "Mo", "Tu", "We", "Th", "Fr", "Sa"]

    days = [31, 29 if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0) else 28,
            31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    for j in range(12):
        print(f"\n  {months[j]} {year}")
        print(" ".join(weekdays))

        print("   " * start_day, end="")

        for k in range(1, days[j] + 1):
            print(f"{k:2} ", end="")
            start_day = (start_day + 1) % 7
            if start_day == 0:
                print()

    print("\n")


def week_day(date):
    """
    Returns the day of the week for a given date.
    """
    yy, mm, dd = map(int, date.split("-"))

    weekdays = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]

    days = [31, 29 if (yy % 4 == 0 and yy % 100 != 0) or (yy % 400 == 0) else 28,
            31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    total_days = sum(days[:mm - 1]) + dd - 1
    start_day = 1

    for year in range(1900, yy):
        start_day += 366 if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0) else 365

    day_week = (start_day + total_days) % 7

    return weekdays[day_week]


def calculate_week_number(date):
    """
    Returns the week number of the given date in a year.
    """
    yy, mm, dd = map(int, date.split("-"))

    days = [31, 29 if (yy % 4 == 0 and yy % 100 != 0) or (yy % 400 == 0) else 28,
            31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    total_days = sum(days[:mm - 1]) + dd
    week_number = (total_days - 1) // 7 + 1
    total_weeks = (366 if days[1] == 29 else 365) // 7 + 1

    return f"Total weeks in {yy}: {total_weeks}\nDate {date} falls in Week {week_number}"


def add_days(date, num_days):
    """
    Adds a given number of days to a date.
    """
    yy, mm, dd = map(int, date.split("-"))
    days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    if (yy % 4 == 0 and yy % 100 != 0) or (yy % 400 == 0):
        days[1] = 29

    while num_days > 0:
        remaining_days = days[mm - 1] - dd
        if num_days > remaining_days:
            num_days -= (remaining_days + 1)
            dd = 1
            mm += 1
            if mm > 12:
                mm = 1
                yy += 1
                days[1] = 29 if (yy % 4 == 0 and yy % 100 != 0) or (yy % 400 == 0) else 28
        else:
            dd += num_days
            num_days = 0

    return f"{yy:04}-{mm:02}-{dd:02}"


def num_of_days(start_date, end_date):
    """
    Returns the number of days between two dates.
    """
    from datetime import datetime
    date_format = "%Y-%m-%d"
    start = datetime.strptime(start_date, date_format)
    end = datetime.strptime(end_date, date_format)
    return (end - start).days


def calculate_week_in_month(date):
    """
    Returns the week number of a date in the month.
    """
    yy, mm, dd = map(int, date.split("-"))
    return f"Date {date} falls in Week {(dd - 1) // 7 + 1} of the month"
