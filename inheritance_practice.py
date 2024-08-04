#  86 _ قسمت 85
#  شی گرایی : تمرین ارث بری
cs = [
    {
        "title": "python",
        "teacher": "Amiri"
    },
    {
        "title": "HTML",
        "teacher": "mohammadi"
    },
    {
        "title": "PHP",
        "teacher": "meri"
    }
]

class User:
    def __init__(self, name):
        self.name = name

    def print_name(self):
        print(f"Name : {self.name}")

##########################################

class Student(User):
    def __init__(self, name, email):
        super().__init__(name)
        self.email = email
        self.cursess = []

    def add_cursess(self, c):
        self.cursess.append(c)

    def print_cursess(self):
        if self.cursess:
            print(f"cursess :  {self.cursess}")
        else:
            print(f"{self.name} don't has cursess.")

    def print_name(self):
        super().print_name()  #  شیوه چند ریختی : اگر این خط کامنت کنم مشکلی ایجاد نمیشه
        print(f"i am a student.\nEmail : {self.email}")

    def pop_cursess(self, number):
        self.cursess.pop(number)

##########################################

class Teacher(User):
    def __init__(self, name, id):
        super().__init__(name)
        self.id = id

    def print_name(self):
        super().print_name()
        print(f"i am a teacher. \nID : {self.id}")
    

t1 = Teacher("ahmad",123)
t1.print_name()


s1 = Student("amir mohammadi","aMohammadi@gmail.com")
s1.print_name()
s1.print_cursess()
s1.add_cursess(cs[0])
s1.print_cursess()
s1.pop_cursess(0)
s1.print_cursess()