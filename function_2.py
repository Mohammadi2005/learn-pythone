#  قسمت 57
#  پارامتر تابع رو یک اشاره گر میزاریم واین باعث میشه تا جا داشته باشه اشاره گر حرکت کنه به تعداد دلخواه بتونیم ورودی بدیم
#  ورودیبه شکل تاپل تبدیل میشه

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
hello_3("hamid","gavad","galil","gahan",age = 19) 


