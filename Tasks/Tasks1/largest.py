list1 = [1,13,2,4,5,66,7,8,6,5,6]

largest = list1[0]

for i in list1:

    if i > largest:

        largest = i

print(f"The largest element is {largest}")