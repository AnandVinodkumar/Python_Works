number = int(input("Enter the number to find factorial of: "))

i = 1

fact = 1

if number < 0:

    print("Please enter a positive number")

else:

    while(i <= number):

        fact *= i

        i += 1

    print(f"Factorial of {number} is {fact}")