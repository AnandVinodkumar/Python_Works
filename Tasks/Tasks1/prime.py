number = int(input("Enter a number: "))

while(number < 1):

    print("Please enter a positive integer.")

    number = int(input("Enter a number: "))

for i in range(2, number):

    if number % i == 0:

        print("Not Prime")

        break

else:

    print("Prime")