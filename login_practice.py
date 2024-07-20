print("part 1. ")

stored_password = "12345"

x = input("Enter your password : ")


if x == stored_password:
    print("Yes you loged in successfully. \n")

else:
    print("Ooo No.")

##############################################
print("part 2. ")

y = input("Enter password : ")
i = 0

while y != stored_password:
    y = input("your password is wrong Enter again : ")
    i += 1
    if i == 3:
        print("you is not user.")
        break

else:
    print("Yes")

##############################################
print("part 3.")

friend = ["amir","saeed","ahmad","ali reza"]

m = "hamed" in friend

print(m)
    

    
    