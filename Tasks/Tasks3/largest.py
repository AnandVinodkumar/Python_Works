def find_max(l):

    largest = l[0]

    for i in l:

        if i > largest:

            largest = i
    
    return largest

n = int(input("Enter the no. of elements in the list: "))

list1 = []

for i in range(n):

    ele = int(input(f"Enter the element {i+1}: "))

    list1.append(ele)

print(f"The largest element in the list is {find_max(list1)}")