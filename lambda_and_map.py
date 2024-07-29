#  قسمت 69

mylist = [1,2,5,9,21]


def func(a):
    return a 

x = map(func, mylist)  #  مپ یک حلقه میزنه و داده ها رو به تابع ای که در ورودی داده ایم قرار میده
print(list(x))  #  چون نوع داده ی ورودی لیست هست پس باید نوع رو هم لیست کنیم

y = list(map(lambda b : b * 2, mylist))
print(y)

mylist_2 = [2,3,5,6,2]

z = list(map(lambda a,b : a * b, mylist, mylist_2))  #  می تونه ورودی ها دو یا چند تا لیست باشن
print(z)

