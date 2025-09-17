def square_list(l):

    l2 = [i**2 for i in l]

    return l2

n = int(input("Enter the no. of elements in the list: "))

list1 = []

for i in range(n):

    ele = int(input(f"Enter the element {i+1}: "))

    list1.append(ele)

print(f"The squared list is {square_list(list1)}")