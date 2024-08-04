#  قسمت  106
#  error handling

try:  #  دستورات این بلاک تا جایی که به خطا نخورن اجرا میشن
    print("hello")
except:  #  اگر دستورات بلاک ترای به خطا بخورن دستورات این بلاک اجرا میشه
    print("Error")

print("-------------------")

try:
    print(4/0)
except:
    print("Error : (4 / 0)")

print("-------------------")

try:  
    print("amir hossein")
    print("mohammadi")
    print(x)
    print("age : 19")
except:
    print("Error")

print("-------------------")

dic = {
    "name": "ahmad reza",
    "age": 19
    }

try:
    print(dic["name"])
except:
    print("Error : we have not key name.")
else:  #  وقتی ترای با موفقیت اجرا بشه اینم اجرا میشه
    print("i am from else block.")

print("-------------------")

try:
    print(dic["school"])
except:
    print("Error : we have not key svhool.")
else:
    print("i am from else block.")

print("-------------------")

#  می تونیم برای یک ارور خاص استثنا بزاریم

try:
    print(x)
except  NameError:
    print("we have name error.")

print("-------------------")

try:
    print(dic["school"])
except  NameError:
    print("we have name error.")
except KeyError:
    print("we have key error.")
