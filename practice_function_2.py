def check_password(password):

    if len(password) < 8:
        print("your password must be at least 8 char")

    elif password.isnumeric():
        print("your password must have at last one letter.")   

    elif password.isalpha():
        print("your password must have at last one number.") 

    else:
        print("tes tath it....!!!.")
        
    
########################################

while True:
    password = input("enter your password : ")
    check_password(password)

