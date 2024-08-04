#  قسمت 74
#  شی گرایی : می تونیم داخل تابع init  عملیات های مختلف قرار بدیم

class My_Class:
    def __init__(self, name, lastname, age, nationality):
        self.name = name
        self.lastname = lastname
        self.age = age
        self.natoinality = nationality

        print(f"person {name} {lastname} is {age} years old.")  #  عملیاتی که توی کانستراکتور انجام میشه
        print(f"he or she is from {nationality}.")

shay1 = My_Class("amir hossein","mohammadi",19,"iran")


#########################################

#  قسمت 75
#  شی گرایی : متد ها برای کلاس ها

class My_Class_2:
    def __init__(self,name,mycar,day,money):
        self.name = name
        self.My_Car = mycar
        self.my_money = money
        self.day = day

    def dabt(self):  #  توی همه ی متد ها باید سلف صدا زده بشه
        if(self.day > 100):
            print(f"the money has doubled : {2*self.my_money}")
        else:
            print(f"your debt is the same as before : {self.my_money}")

ob = My_Class_2("reza","perayd",110,200)
ob.dabt()
    
#########################################

#  قسمت 76
#  شی گرایی : حذف کردن یک پراپرتی  

print(ob.name)

del ob.name

print(ob.name)  #  چون در خط قبلی پراپرتی رو حذف کردم اینجا خطا میده