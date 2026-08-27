# Python Datetime Module Practice

from datetime import datetime, date, timedelta

now = datetime.now()

print("Current date and time:", now)
print("Current date:", date.today())
print("Year:", now.year)
print("Month:", now.month)
print("Day:", now.day)

tomorrow = date.today() + timedelta(days=1)
print("Tomorrow:", tomorrow)

next_week = date.today() + timedelta(days=7)
print("Next week:", next_week)
