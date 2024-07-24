#  stackoverflow

myname = input("enter your name : ")
myname = myname.lower()
myname = myname.replace(" ","")  #  با این حرکت همه اسپیس ها رو حذف می کنم
print(myname)

n = []
for m in myname:  #  توی این حلقه تایپ m از نوع str هست
    if m not in n:
        print("your name has " + str(myname.count(m)) + "   " + m )
    n.append(m)

