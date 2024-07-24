#########################################
#  تمرین 1

friends = ["amir","mohammad","saeed","ahmad","hh"]
friends_1 = []

for name in friends:
    if name[len(name) - 1] == "d" or name[0] == "a":  #  name[-1]
        friends_1.append(name)
        friends_1.insert(len(friends_1),name)

print(friends_1)

##########################################
#  تمرین 2

a = ["amir","jamal","vahid","karim","saeed","ahmad reza"]
b = ["amir","mohammad","saeed","ahmad","hh"]

for name in b:
    for name_2 in a:
        if name_2 == name:
            print(name)