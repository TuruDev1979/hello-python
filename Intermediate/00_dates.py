### Dates ###

# Importamos la funcion datetime de datatime
from datetime import datetime

now = datetime.now()

def print_date(date):
    print(f"{date.day}/{date.month}/{date.year}")
    print(now.minute)
    print(now.second)
    print(now.timestamp())

print_date(now)

year_2023 = datetime(2023, 1, 1)

print_date(year_2023)

# Importamos la funcion time de datatime
from datetime import time

current_time = time(18, 24, 36)

print(current_time.hour)
print(current_time.minute)
print(current_time.second)

# Importamos la funcion date de datatime
from datetime import date

current_date = date.today()

print(current_date.day)
print(current_date.month)
print(current_date.year)

# Operciones con fechas
from datetime import timedelta
current_date = date(current_date.year, current_date.month, current_date.day)
date_two = date(current_date.year, current_date.month + 3, current_date.day)

# Restar fechas
diff = date_two - current_date
print(current_date)
print(date_two)
print(diff)

# Sumar a una fecha días  (timedelta weeks, days, hours, minutes, seconds, milliseconds y microseconds)
result = current_date + timedelta(days=365)
print(result)