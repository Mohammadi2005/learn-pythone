
number = int(input("enter ane number betwen 1 and 9 : "))  # تایپ ورودی همیشه استرینگ خواهد بود
x = number

x *= 2
# x = "amir" * 4
x += 8
x += number
x -= 2
x /= 3  # از اینجا تایپ میشه float 
x -= number
x *= 4

print(x)

# python lists

mylist = ['reza',"ali","amir","ahmad"]
print(type(mylist))  # type list
print(mylist)
print(len(mylist))

newlist = ["amir", 3, 5.8, False]  # ایتم های داخل لیست ها می تونن از انواع متفاوت باشند
print(newlist[1])
print(type(newlist[1]))

print(mylist[2:4])
print(newlist[0:2])
print(mylist[:3])
print(mylist[1:])

newlist_1 = mylist[2:4]

# change items

mylist[0] = "mohammad"
print(mylist)

mylist[1:3] = ["mahdi","saeed"]
print(mylist)
print(len(mylist))

mylist[0:1] = ["mohammad","hossein"]
print(mylist)
print(len(mylist))

mylist[0:2] = ["mohammad"]
print(mylist)
print(len(mylist))

# add items

mylist.append("amir")  # اضافه میکنه به انتها
print(mylist)
print(len(mylist))

mylist.insert(0,"maten")  #  افزودن عنصر در مکان دلخواه
print(mylist)
print(len(mylist))  

mylist.extend(newlist)  # یک لیست رو به لیست دیگه اضافه میکنه
print(mylist)
print(len(mylist))

mytuplle_2 = ("ysef","iran")  #  تیوپل ها اعضاشون قابل تغییر نیستند 
mylist.extend(mytuplle_2) 
print(mylist)
print(len(mylist))

list3 = mylist + newlist
print(list3)

# remove items

mylist.remove("amir")  # حذف براساس مقدار
print(mylist)
print(len(mylist))

#mylist.remove("x")
#print(mylist)
#print(len(mylist))

mylist.pop(0)
print(mylist)
print(len(mylist))

mylist.pop() #  اگر شماره اندیس نذاریم اخری رو حذف میکنه
print(mylist)
print(len(mylist))

newlist.clear()  #  لیست رو خالی میکنه 
print(newlist)
print(len(newlist))

del newlist #  لیست رو کلا حذف میکنه
# print(newlist)
