name = "pYtHoN"

#print(name.swapcase())

new = ""

for i in name:

    if i.islower():

        new += i.upper()

    else:

        new += i.lower()

print(new)