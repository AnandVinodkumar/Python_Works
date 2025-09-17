list1 = [1,2,3,4,5,6,7,8,9,10]

for i in range(len(list1)):

    ele = list1.pop(i)

    sq = ele ** 2

    list1.insert(i,sq)

print(list1)