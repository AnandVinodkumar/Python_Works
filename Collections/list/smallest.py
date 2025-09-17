numbers = [7,4,9,5,3,2,11,2,5]

#WAP to find the smallest without min() function

smallest = numbers[0]

for i in numbers:

    if i < smallest:

        smallest = i

print(f"The smallest element is {smallest}")    #2