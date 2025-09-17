def second_largest(numbers):

    largest = numbers[0]

    sec_largest = numbers[1]

    for i in numbers:

        if i > largest:

            sec_largest = largest

            largest = i

        elif i > sec_largest and i != largest:

            sec_largest = i
    
    print(f"The second largest number is: {sec_largest}")

numbers = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]

second_largest(numbers)