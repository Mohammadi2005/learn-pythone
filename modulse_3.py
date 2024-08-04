#  قسمت 91 
#  مازول ها : چطور می تونم تایم یک منطقه خاص  رو داشته باشم

from datetime import *
import pytz 

x = datetime.now()
print(x)

q = pytz.timezone("Asia/Gaza")  #  تایم توی غزه رو میده
z = datetime.now(q)
print(z)  

tz = pytz.timezone("America/Los_Angeles")  #  تایم لس انجلس رو میده
y = datetime.now(tz)
print(y)


