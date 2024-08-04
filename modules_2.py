#  قسمت  89
#  برخی از مازول ها به صورت پیش فرض توی پایتون هستند

import platform
import random

print(platform.system())
print(platform.processor())

print(random.randint(0,100))  # یک عدد رندوم از بین 100 و 0 میده

mylist = ['ali','amir','saeed','ahmad']

print(random.choice(mylist))  #  یک ایتم به صورت رندوم از داخل لیست انتخاب می کنه

print("------------------------------")

#  قسمت  90

from datetime import *

x = datetime.now()  #  تاریخ کنونی توی ایکس ریخته میشه
print(x)
print(x.year)
print(x.minute)

y = datetime(2005,2,5)
print(y)

print(x.strftime("%A"))  #  روز هفته رو میده
print(x.strftime("%B"))  #  نام ماه رو میده

