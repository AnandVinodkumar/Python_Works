string1 = "I love python"

string2 = ""

list1 = string1.split()

list2 = []

for i in list1:

    list2.append(i[::-1])

for j in list2:

    print(j, end=" ")