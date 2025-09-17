"""
A spy number is a number where the sum of its digits is equal to the product of its digits.
For example, 1124 is a spy number because 1 + 1 + 2 + 4 = 8 and 1 * 1 * 2 * 4 = 8
"""
number = int(input("Enter a number: "))

sum = 0

prod = 1

for i in str(number):

    sum += int(i)

    prod *= int(i)

if sum == prod:

    print(f"{number} is a spy number.")

else:

    print(f"{number} is not a spy number.")