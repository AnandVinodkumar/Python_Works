list1 = [1,2,3,4,5,6,7,8,9]

k = int(input("How many times do you want to rotate the list to the right?: "))

while(k > 0):

    last = list1.pop()

    list1.insert(0,last)

    k -= 1

print(list1)

