#  قسمت 67
#  لامبدا ها توابع یک خطی هستند که توی یک متغییر ریخته میشن و برای صدا زدنشون باید متغییر رو صدا بزنیم

def myfunc(number):
    return number + 14

print(myfunc(2))

x = lambda a : a + 14

print(x(2))

y = lambda a,b,c : a + b + c 

print(y(6,7,4))

##################################

#  قسمت 68
#  چرا باید از لامدا ها استفاده کنیم

def func(n):
    def new(m):  #  داخل یک تابع میتونیم یک تابع دیگه تعریف کنیم
        return n * m
    
    return new  #  خروجی یک تابع میتونه یک تابع باشه

func_2_barabar = func(2)  #  تبدیل میشه به تابعی که یک عدد رو دوبرابر می کنه

print(func_2_barabar(3))

print(func(2)(3))

func_3_barabar = func(3)  #  تبدیل میشه به تابعی که یک عدد رو سه برابر می کنه

print(func_3_barabar(5)) 

#  نکته : تابع نیو رو میشه به صورت لامدا تعریف کنیم

def func_lambda(n):  
    return lambda a : a * n

func_lambda_2_barabar = func_lambda(2)  #  تبدیل میشه به لامدایی که یک عدد رو دوبرابر می کنه
#  func_lambda_2_barabar == lambda n : n * 2

print(func_lambda_2_barabar(7))
