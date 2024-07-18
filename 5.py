#  tuples
#  سرعتشون از لیست ها بیشتره 
#  ایتم هاشون قابل تغییر نیستند 
#  با پرانتز ایجاد میشن  ()

mytuple = ("amir","reza","ali","mahdi")
print(mytuple)
print(type(mytuple))

mylist = list(mytuple)
mylist[1] = "mohammad"
print(mylist)

mytuple = tuple(mylist)

newtuple = (1,True,347,77,3)

tuple3 = newtuple + mytuple

print(tuple3)

string = ("farid")  # یک عضوی بدون کاما میشه استرینگ
print(type(string))  

tuple4 = ("farid",)  # یک عضوی با کاما میشه تاپل
print(type(tuple4)) 