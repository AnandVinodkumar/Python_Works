"""
A neon number is a positive integer where the sum of the digits of its square equals the original number

"""
number = int(input("Enter a number: "))

new = number ** 2

sum = 0

for i in str(new):

    sum += int(i)

if sum == number:

    print(f"{number} is a neon number.")

else:

    print(f"{number} is not a neon number.")