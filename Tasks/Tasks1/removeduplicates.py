list1 = [1,1,2,3,4,4,4,4,5,5,5,56,6,6,6,6]

for i in list1:

    while(list1.count(i) > 1):

        list1.remove(i)

print(list1)