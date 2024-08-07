#  قسمت 57
#  پارامتر تابع رو یک اشاره گر میزاریم واین باعث میشه تا جا داشته باشه اشاره گر حرکت کنه به تعداد دلخواه بتونیم ورودی بدیم
#  ورودی به شکل تاپل تبدیل میشه

def hello(name_1,name_2):
    print(f"hello {name_1} and {name_2}.")

hello("amir","ali")

def Hello(*arg):  #  هر تعداد ورودی بخوایم میتونیم بهش بدیم
    print(arg)
    for i in arg:
        print(f"hello {i}")

Hello("amir","akbar","vahid","saeed")  
Hello()

def hello_2(name_1,name_2,*name):  #  حداقل دوتا ورودی باید داشته باشه
    print(f"hello {name_1} and {name_2}.")
    for i in name:
        print(f"hello {i}")

hello_2("A","B","c","d","e")

######################################

#  قسمت 58
#  چطور ارگومان غیر ضروری به تابع بدیم
#  اول باید یک پارامتر با استار و یک پارامتر با دو تا استار بهش بدیم
#  تک استار تایپش تاپل هست و دابل استار تایپش ساختار هست و باید هراه با کلید باشه و از قوانین تاپل و ساختار پیروی می کنن

def hello_3(name_1,name_2,*date_arg,**date_kwargs):  
    print(name_1)
    print(name_2)
    print(date_arg)
    print(date_kwargs)
    
hello_3("ahmad","kamal")
hello_3("hamid","gavad","galil","gahan",age = 19,year = 1403) 

#######################################

#  قسمت 59
#  Default value
#  پارامتر های یک تابع رو به صورت پیش فرض مقدار دهی میکنیم

# def me(name = "amir hossein", last_name = "mohammadi"):
#     print(f"my name is {name} {last_name}.")

# me("ahmad reza")
# me()
# me("saeed","akbari")

# #######################################

# #  قسمت 60
# #  Passing a list as a argument
# #  هر نوع داده ای رو می تونیم به تابع پاس بدیم

# def hello_list(mylist):
#     for item in mylist:
#         print(f"hello {item}")

# list_1 = ["ali","ahmad","ahsan","mohsan"]

# hello_list(list_1)
# print("\n\n")
# hello_list(["amir","gavad"])
# print("\n\n")
# hello_list("amir ali")  #  string ها هم لیبست هستند

# ######################################

# #  61 قسمت
# #  return values
# #  با کلمه ریترن مقدار دلخواه رو میفرستیم تو خروجی

# def sum(a, b):
#     c = a + b
#     return c

# print(sum(44,8))
# print(sum(14,5) + 20)

# def SUM(a,b):  #  میتویم چندین مقدار برای خروجی داشته باشیم
#     return a + b, a * b, a, b  #  مقادیر خروجی توی تاپل ذخیره میشه

# print(SUM(3,4))

# for i in SUM(5,2):
#     print(i)

# print("\n\n")

# result = SUM(1,6)

# for i in result:
#     print(i)
