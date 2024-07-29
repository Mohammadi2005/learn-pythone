#######################################

#  قسمت 62
#  

username = input("enter yuor username : ")

def validation(Username):
    if len(Username) > 8:
        return False
    
    else:
        return True
    
if not validation(username):
    print("Yes")

else:
    print("No")

########################################

#  قسمت 63
#  تمرین تابع : تعداد حروف بزرگ و کوچیک رو مشخص کن


def n_chars(string):

    upper = sum(1 for c in string if c.isupper())
    lower = sum(1 for c in string if c.islower())
    return lower,upper

print(f"lowers : {n_chars(username)[0]}")
print(f"uppers : {n_chars(username)[1]}")

def number_chars(string):
    upper = 0
    lower = 0
    for i in string:
        if i.islower():
            lower += 1

        elif i.isupper():
            upper += 1

    print(lower,upper)

#  while True:
#  username = input("enter yuor username : ")

number_chars(username)

########################################

#  قسمت 64
#  تمرین تابع : 

def number_type(num):
    if num % 2 == 0:
        print("this is a even number.")
    
    elif num % 2 == 1:
        print("this is a odd number.")
    
num = int(input("enter ane number : "))
number_type(num)
