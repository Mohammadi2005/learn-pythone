def check_number(password):    #  isnumeric()
    return any(i.isdigit() for i in password)

def check_char(password):   #  isalpha()
    return password.isdigit()

#####################################

password = input("enter your password : ")

if len(password) < 8:
    print("your password must be at least 8 char")
    password = input("enter your password again : ")

if not check_number(password):
    print("your password must have at least one number.")
    password = input("enter your password again : ")

if check_char(password):
    print("your password must have at last one letter.")
    password = input("enter your password again : ")

else:
    print("tes tath it....!!!.")

