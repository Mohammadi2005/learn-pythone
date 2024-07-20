print("part 1. ")
users = {
    "amir": "2005",
    "ahmad": "2003",
    "mohammad": "2014"
}

entered_username = input("enter your user name : ")
entered_password = input("enter your password : ")


if entered_username in users and users[entered_username] == entered_password: # اول بررسی میکنیم کلید وجود داره یا نه اگر وجود داشت بعد بررسی می کنه ایا مقدار اون کلید هم وجود داره یا نه
    print("yeeesssssssss you is our user. ")

else:
    print("ohhhhhhhhhh nnooooooo you is not our user. ")

############################################
print("part 2. \n")

while entered_username not in users:
    entered_username = input("enter your user name again : ")

else:
    entered_password = input("enter your password : ")
    i = 0
    while users[entered_username] != entered_password:
        entered_password = input("enter your password again : ")
        i += 1
        if i == 3:
            print("Error you is not our user. ")
            break
    
    else:
        print("you login saccessfully. ")