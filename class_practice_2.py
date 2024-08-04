#  79 _ قسمت 78
#  شی گرایی : تمرین
#  می تونیم پراپرتی مشترک بین همه اشیای یک کلاس داشته باشیم

class persons:

    number_persons = 0  #  پراپرتی مشترک بین همه اشیای کلاس

    def __init__(self, name, age):
        self.name = name
        self.age = age
        persons.number_persons += 1

    def date(self):
        print(f"{self.name} is {self.age} years old.")

print(persons.number_persons)  #  از طریق نام کلی خود کلاس می توان به پراپرتی مشترک دسترسی داشت
p1 = persons("ali",51)
print(persons.number_persons)
p2 = persons("amir",21)
print(persons.number_persons)
p3 = persons("ahmad",23)
print(persons.number_persons)

print("\n")

p3.number_persons = 8  #  از طریق خود اشیا هم می توان به پراپرتی مشترک دسترسی داشت ولی تغییرات فقط مختص به خود ان شی هست 
#  اگر پراپرتی مشترک کلاس رو از طریق شی تغییر بدیم روی بقیه تاثیری نداره

print(p1.number_persons)
print(p2.number_persons)
print(p3.number_persons)

print("\n")

persons.number_persons = 111  #  تغییراتی که توی پراپرتی مشترک از طریق خود شی ایجاد میشه نسبت به خود کلاس اولویت داره
#  اگر پراپرتی مشترک کلاس رو از طریق کلاس تغییر بدیم روی بقیه تاثیری داره

print(p1.number_persons)
print(p2.number_persons)
print(p3.number_persons)
