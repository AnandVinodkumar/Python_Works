list1 = [1,2,3,4,5]

list2 = [6,7,8,9,10]

while(list2 != []):

    first = list2.pop(0)

    list1.append(first)

print(list1)