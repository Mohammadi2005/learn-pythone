first_name = 'amir hossein'
last_name = "mohammadi"

my_name = "my name is : " + first_name + " " + last_name
print(my_name)

date = 'i am amir hossein \ni am from iran'
print(date)

password = "word \'AHM\' is passwprd" # همراه با بک اسلش باید بیاد استفاده از سینگل کوتیشن داخل منن
print(password)

text = """hello
i am from iran
from mashhad""" # دیگه نیازی به بک اسلش ان نداریم
print(text)

# Slicing string

n = 'probe'
print(n[0] + "\n" + n[4] + "\n" + n[1])
print('probe'[2])

m = "ahmad reza mohammadi"
print(m[2:13]) # برش میزنه

print(m[:13])

print(m[2:])

print(m[-4:-1])

print(m[-12:-9])

age = 20
txt = "my age is : " + str(age) # روش 1
print (txt)

txt_1 = f"my age is : {age}" #فرمت اسرینگ روش 2
print(txt_1)

# string methods

text  = "   i am {} {} From Iran    "

print(text.capitalize()) # اولین حرف رو بزرگ میکنه
print(text.casefold())  # همه حروف رو کوچک میکنه
print(text.count("i")) # تتعداد دفعاتی که حرف تکرار شده رو نشون میده
print(text.find("a")) 
print(text.index("a"))
print(text.format("amir hossein","mohammadi")) # اکولاد ها رو مقدار دهی میکنه
print(text.strip()) # اسپیس های اضافی رو از دو طرف حذف میکنه
print(text.title()) # حرف اول ها رو بزرگ میکنه
print(text.upper())  # همه حروف رو بزرگ میکنه
print(text.lower()) # همه حروف رو کوچیک میکنه
print(len(text)) #  طول رشته رو میده

# date type bool

print(bool("amir"))
print(bool(text))
print(bool(20))
print(bool(""))
print(bool(0))
print(bool(None))
print(bool(()))

print( 1 == 4 )
print( 1 != 4)

print( 1 > 4 )
print( 1 < 4 )

i = 1 == 4
print(i)
print(type(i))

new_pass1 = 1383
new_psss2 = 2005

print(new_pass1 == new_psss2)








