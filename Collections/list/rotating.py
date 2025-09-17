numbers = [1,2,3,4,5,6] #   numbers = [6,1,2,3,4,5]

n = int(input("Enter the count: "))

for i in range(n):  #i = 0,1,2

    numbers.insert(0,numbers.pop())

    # last_item = numbers.pop()

    # numbers.insert(0,last_item)

print(numbers)
