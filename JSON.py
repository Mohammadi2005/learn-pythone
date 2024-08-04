#  قسمت 94 و 95
#  فرض کن یک سایت با سعید جان زدی که فرانت رو تو زدی با جاوا و بکند رو سعید زده با پایتون
#  جیسون یکی از فرمت ها هست که مثل مترجم برای دو زبان عمل می کنه 

##################################

#  قسمت  98
import json

x = '{"fname":"amir","lname":"mohammadi","age":19,"city":"mashhad","job":"student","isTeacher":false}'  #  فرمت جیسون

print("format JSON :")
print(type(x))
print(x)

y = json.loads(x)  #  فرمت جیسون رو به پایتون تبدیل میکنه

print("format python :")
print(type(y))
print(y)

z = json.dumps(y)  #  فرمت پایتون رو به جیسون تبدیل میکنه

print("format JSON again :")
print(type(z))
print(z)