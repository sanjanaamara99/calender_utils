from calendar_utils import yearly_calendar, week_day, calculate_week_number, add_days, num_of_days, calculate_week_in_month

# Test yearly calendar
yearly_calendar(2025)

# Get the day of the week for a given date
print(week_day("2025-01-17"))

# Calculate the week number for a given date
print(calculate_week_number("2024-01-17"))

# Add days to a date
print(add_days("2025-01-16", 50))

# Calculate days between two dates
print(num_of_days("2025-01-16", "2025-03-07"))

# Calculate the week in a month
print(calculate_week_in_month("2024-01-17"))
