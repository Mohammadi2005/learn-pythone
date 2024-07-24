####################################
print("part 1. \n")

friends = ["amir","mohammad","saeed","ahmad"]

print(len(friends))

for item in friends:
    print("hi " + item)
    print(len(item))

####################################
print("part 2. \n")

myname = "amir hossein"

for char in myname:
    if char == " ":
        #break
        continue
    print(char)

####################################
print("part 3. \nrange function.")

for numbe in range(4):
    print(numbe)

print("\n\n")

for x in range(20,23):  #  تعیین محدوده
    print(x)

print("\n\n")

for x in range(2,15,4):
    print(x)
else:
    print("finished")
