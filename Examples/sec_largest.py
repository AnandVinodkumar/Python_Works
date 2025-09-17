numbers = [1,2,3,4,5,6,7,-1,-5]

count = 2

largest = 0

while(count != 0):

    for i in numbers:

        if i > largest:

            largest = i

    ele = numbers.pop(numbers.index(largest))

    largest = 0

    count -= 1

print(f"The second largest element is {ele}")