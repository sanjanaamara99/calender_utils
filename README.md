# calender_utils

calendar_utils - Python Library Documentation
Project Description
calendar_utils is a Python library designed to offer a comprehensive suite of calendar-related functions. This library provides functionalities such as printing a yearly calendar, determining the day of the week for a specific date, calculating week numbers in a year and month, adding days to a date, and finding the number of days between two dates.
Features
- Print Yearly Calendar: Display the calendar for a given year.
- Determine Weekday: Find out the day of the week for a specific date.
- Calculate Week Number in Year: Get the week number for a given date in a year.
- Add Days to Date: Calculate a new date by adding a specified number of days to an existing date.
- Calculate Days Between Dates: Find the number of days between two dates.
- Calculate Week in Month: Determine the week number for a date within its month.
Installation
You can install this library using pip:
pip install calendar_utils
Usage
Here's how you can use the functions provided by calendar_utils:
Import the Library
from calendar_utils import (
    yearly_calendar,
    week_day,
    calculate_week_number,
    add_days,
    num_of_days,
    calculate_week_in_month
)
Print Yearly Calendar
yearly_calendar(2025)
Determine Weekday
print(week_day("2025-01-17"))
Calculate Week Number in Year
print(calculate_week_number("2024-01-17"))
Add Days to Date
print(add_days("2025-01-16", 50))
Calculate Days Between Dates
print(num_of_days("2025-01-16", "2025-03-07"))
Calculate Week in Month
print(calculate_week_in_month("2024-01-17"))
Project Structure
calendar_library/
│── calendar_utils/
│   ├── __init__.py
│   ├── calendar_functions.py
│── setup.py
│── main.py
│── test.py
