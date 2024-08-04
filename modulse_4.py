#  قسمت  92
#  فرض کن یک وب سایت زدی و توش افراد میان اشتراک یک ماهه می خرن می خوایم ببینیم چطور می شه تایم باقی مونده تا پایان اشتراک رو بفهمیم
from datetime import *

start = datetime(2024,7,5)  #  این تایم اغاز اشتراک هست
end = start + timedelta(days=30)  #  تایم پایان اشتراک رو میده و می تونیم بر اساس ساعت هم بدیمش
now = datetime.now()
remain = end - now  #  زمان باقی مونده رو میده

print(f"your start time : {start}")
print(f"your time at {end} will finshed.")
print(f"remain time : {remain}")  

