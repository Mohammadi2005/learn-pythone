#  قسمت 65
#  تمرین تابع : تبدیل تاریخ شمسی به میلادی

year = int(input("Enter year : "))
month = int(input("Enter month : "))
day = int(input("Enter day : "))

def converter(year,month,day):

    year += 621
    month += 2
    day -= 10

    if month == 10 and day > 10 or month > 10:
        year += 1

    if day > 10:
        month += 1

    month %= 12

    if day < 1 and month < 7:
        day += 31

    elif day < 1 and month > 6:
        day += 30

    print(f"your date to meladi is : {year} / {month} / {day}")

converter(year,month,day)

