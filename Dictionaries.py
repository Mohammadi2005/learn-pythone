#  همون ساختار ها توی سی و سی پلاس پلاس هستند

me = {
    "first name": "amir hossein",
    "last name": "mohammadi",
    "age": 19.5,
    "list friends": ["saeed","mohammad","ahmad"]
}

print(type(me))
print(me)
print(me["age"])
print(me.get("age"))
print(me["list friends"])
print(len(me))

#  لیست کلید ها رو بر می گردونه

print(me.keys())

#  لیست مقادیر رو برمی گردونه

print(me.values())

#  هر ایتم رو داخل یک تاپل می زاره و کل ساختار می زازه داخل یک لیست

print(me.items())

#  چک کردن

print("list friends" in me) 
print("name" in me)

#  تغییر اعضا

me["age"] = 20
me["first name"] = "Amir hossein"

me["id"] = 929   # اگر کلید وجود نداشته باشه به ساختار ایتم اضافه میشه 

print(me)