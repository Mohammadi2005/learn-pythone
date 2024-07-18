#  همون مجموعه ها در ریاضی هستن
#  داخل اکولاد ایجاد میشن {}
#  نظم و اندیس ندارند 
#  ایتم ها قابل تغییر نیستند ولی میشه کم و زیادشون کرد 
#  نمیشه ایتم تکراری براش استفاده کرد

myset = {"ali","reza","amir"}

print(myset)

print(myset)

myset1 = {"mohammad","mohammad","mohammad"}
print(myset1)

print("ali" in myset) #  میتونیم ببینیم عضو هست یا نه
print("ahmad" in myset)

# add item 

myset.add("saeed")
print(myset)

# add list to list 

myset.update(myset1)
print(myset)

mylist = ["karim","gavad"]

myset.update(mylist)  #  می تونیم لیست و تاپل رو به ست اضافه کنیم
print(myset)

#  remove items

myset.remove("ali")
print(myset)

#  myset.remove("taha")  #  اگر عضو ست نباشه خطا میده
#  print(myset)

myset.discard("karim")
print(myset)

myset.discard("taha")  #  اگر عضو ست نباشه خطا نمیده
print(myset)

#  union sets 

myset2 = {1,12,32,556}

myset3 = myset.union(myset2)  #  اجتماع میگیره
print(myset3)

print(myset2 | myset)  #  اجتماع میگیره

myset.intersection_update(myset1)  #  اشتراک میگیره
print(myset)

myset3 = myset.intersection(myset1)  #  اشتراک میگیره
print(myset3)

print(myset & myset1)  #  اشتراک میگیره

myset4 = {1,54,84,12}

myset5 = myset4.symmetric_difference(myset2)
print(myset5)

myset4.symmetric_difference_update(myset2)  #  نا مشترک ها رو میگیره
print(myset4)

#  clear items

myset.clear()
print(myset)



