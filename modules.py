#  قسمت 88
#  توی پروزه های بزرگ تعداد خطوط کد زیاده و حرفه ای نیست که همه ی کد ا توی یک فایل قرار بگیرن
#  باید بخش های مختلف پروزه رو توی فایل های مختلف قرارر داد

def me(name,age):
    print(f"i am {name}\ni has {age} years old.")

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

class User:
    pass

x = 101