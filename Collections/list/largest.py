numbers = [7,4,9,5,3,2,11,2,5]

#WAP to find the largest without max() function

largest = numbers[0]

for i in numbers:

    if i > largest:

        largest = i

print(f"The largest element is {largest}")

numbers.reverse()

print(numbers)