#  sort list 

mylist = ['reza',"ali","amir","ahmad","Ali reza"]

mylist.sort()  #  بر اساس حرف الفبا مرتب می کنه
print(mylist)

mylist.sort(reverse = True)  #  بر عکس حروف الفبا مرتب می کنه
print(mylist)

mylist_number = [2,8,145,6,1,4]

mylist_number.sort()
print(mylist_number)  #  از کوچیک به بزرگ مرتب میشه

mylist_number.sort(reverse = True)  #  از بزرگ به کوچیک مرتب می کنه
print(mylist_number)

# copy list 

newlist = mylist.copy()
print(newlist)

