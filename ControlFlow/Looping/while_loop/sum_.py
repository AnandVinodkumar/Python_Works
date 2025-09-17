name = "qwert65354yys$#21" #total = 26

sum = 0

i = 0

while(i < len(name)):

    if name[i].isdigit():

        sum = sum + int(name[i])

    i += 1

print(sum)