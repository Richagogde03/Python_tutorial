from datetime import datetime
from datetime import time
from datetime import timedelta


# datetime class
now = datetime.now()
print(now)
# creating a specified datetime
specific_date = datetime(2025, 12, 25, 10, 30, 0)
print(f"Specific datetime: {specific_date}")


# time class
break_time = time(1, 30, 0)
print(f"Break time = {break_time}")
print(f"Break time hour : {break_time.hour}")
print(f"Break time hour : {break_time.minute}")


# timedelta class
duration = timedelta(days=5, hours=3)
print(f"Duration: {duration}")

future_date = now + duration
print(f"Date in 5 days and 3 hours : {future_date}")

past_date = now - timedelta(weeks=2)
print(f"Date two weeks ago : {past_date}")

date1 = datetime(2025, 2, 15)
date2 = datetime(2025, 4, 10)
difference = date2 - date1
print(f"Difference between future and past date : {difference}")
