#  قسمت 77
#  شی گرایی : تمرین

class car:
    def __init__(self, name, price):
        self.name = name
        self.price = price
        self.status = False

    def start(self):
        if self.status:
            self.status = True
            print(f"{self.name} is being started.")
        else:
            print(f"{self.name} is turn on.")

    def off(self):
        if not self.status:
            self.status = False
            print(f"{self.name} is being off.")
        else:
            print(f"{self.name} is turn off.")

car1 = car("benz",200)
car2 = car("pezho",20)

car1.start()
car1.start()
car1.off()

print(not car1.status)

