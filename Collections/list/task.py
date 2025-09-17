#Reverse letters
#input >> "learn python with fun"
#output >> "nrael nohtyp htiw nuf"

# name = "learn python with fun"

# items = name.split()

# new = ""

# for i in items:

#     new += i[::-1] + " "

# print(new)

name = "learn python with fun" #op: "fun with python learn"

name = name.split()

new = ""

# for i in name[::-1]:

#     new += i + " "

"""
                                                #-4       -3       -2     -1
# for i in range(-1,-(len(name)+1),-1):      #['learn', 'python', 'with', 'fun']

#     new += name[i] + " "

"""


for i in name:

    new = i + " " + new



print(new)