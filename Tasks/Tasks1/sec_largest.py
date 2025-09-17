list1 = [10,9,8,7,6,5,4,3,2,1]

largest = list1[0]

sec_largest = list1[1]

for i in list1:

    if i > largest:

        sec_largest = largest

        largest = i

    elif i < largest and i > sec_largest:

        sec_largest = i

print(f"The second largest element is {sec_largest}")