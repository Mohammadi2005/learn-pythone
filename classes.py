#  قسمت 72
#  شی گرایی و کلاس

class My_Class:  #  حروف اول نام کلاس باید بزرگ باشن این یک قانون نا نوشته هست
    def __init__(self):  #  self متغییر نام شیب هست
        self.name = "amir"  
        self.lastname = "mohammadi"

p1 = My_Class()  #  ساخت شی
p2 = My_Class()

print(p1.name)

p2.name = "ahmad"

print(p2.name)


###################################

#  قسمت 73
#  شی گرایی و کلاس

class My_Class_2:
    def __init__(self, name, lastname):  #  constractor
        self.Name = name
        self.Lastnme = lastname

o1 = My_Class_2("ali","dorraki")  #  ساخت یک شی

print(f"{o1.Name} {o1.Lastnme}")

