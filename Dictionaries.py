#  همون ساختار ها توی سی و سی پلاس پلاس هستند

me = {   # me هست یک اشاره گر
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

print("list friends" in me)  #  bool
print("name" in me)  #  bool

#  تغییر اعضا

me["age"] = 20
me["first name"] = "Amir hossein"

me["id"] = 929   # اگر کلید وجود نداشته باشه به ساختار ایتم اضافه میشه 

print(me)

#  حذف ایتم از دیکشنری

me.pop("first name")
print(me)

me.popitem()  #  اخرین عنصر اضافه شده رو حذف می کنه
print(me)

del me["last name"]
print(me)

#  کپی کردن ساختار

me1 = me  #  ادرس me میره تو me1         /        این روش برای کپی کردن درست نیست

print(me1["age"])
me["age"] = 21  #  me رو تغییر میدم ولی تغییرات توی me1 هم ایجاد میشه چون ادرسشون یکی هست
print(me1["age"])

me2 = me.copy()  # روش صحیح کپی کردن

print(me2)
me["age"] = 22  #  تغییرات توی me2 ایجاد نمیشه چون ادرسشون یکی نیست
print(me2)

me3 = dict(me)
print(me3)  #  روش دوم کپی کردن

me3["color"] = "red"
print(me3)
print(me)

#  ساختار های تو در تو

myfamily = {

    "name fader": "mohammad mohammadi",

    "child1": {
        "name": "ahmad reza",
        "age": 22
    },
    "child2": {
        "name": "amir hossein",
        "age": 20
    },
    "child3": {
        "name": "fateme",
        "age": 10
    }
}
print(myfamily["name fader"])

print(myfamily["child1"])
print(myfamily["child2"]["name"])
print(myfamily["child3"]["age"])

chaild_2 = myfamily["child2"]
print(chaild_2)
print(myfamily["child2"])

keys = ('key1','key2','key3')
valus = 1

mydict = dict.fromkeys(keys,valus)  #  ساختار رو میسازه و همه مقادیر ئرو با یک مقدار مقدار دهی میکنه  
print(mydict)