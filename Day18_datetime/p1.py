# Get the current day, month, year, hour, minute and timestamp from datetime module

from datetime import datetime

now = datetime.now()
print(now)
day = now.day
month = now.month
year = now.year
min = now.minute
print(f"{year}/{month}/{day}")
print(f"{min}")
timestamp = now.timestamp()
print(timestamp)