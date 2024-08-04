# 84 _ 83 _ قسمت 81 _ 82
#  شی گرایی : ارث بری

class Person:  #   حواست باشه وقتی یک کلاس میسازی با حرف بزرگ شروع کنی
    def __init__(self ,fname, lname):
        self.fname = fname
        self.lname = lname

    def printname(self):
        print(f"{self.fname} {self.lname}")


class Student(Person):  #  شیوه ارث بردن
    
    def __init__(self, fname, lname, age, school):

        #  Person.__init__(self, fname, lname)  #  پاس میده به کانستراکتور کلاس پدر
        super().__init__(fname, lname)  #  پاس میده به کانستراکتور کلاس پدر
        #  به صورت خود کار به کلاس پدر اشاره می کنه super
        #  هر دو خط بالا یک کار رو می کنن ولی بهتره از  super  استفاده بکنیم
        self.age = age
        self.school = school

    def print_age_school(self):
        print(f"Name : {self.fname} {self.lname} \nAge : {self.age} \nSchool : {self.school}")

s1 = Student("ali", "ahmadi", 11, "AAA")
s1.printname()
print(s1.age)
s1.print_age_school()



