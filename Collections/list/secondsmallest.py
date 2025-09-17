numbers = [10,1,9,2,8,3,7,4,6,5]

smallest = numbers[0]

sec_smallest = numbers[1]

for i in numbers:

    if i < smallest:

        sec_smallest = smallest

        smallest = i

    elif i < sec_smallest:

        sec_smallest = i

print(sec_smallest)