# number = int(input("Enter a number: "))

# if number > 1:

#     for i in range(2,number):

#         if number % i == 0:

#             print(f"{number} is not a prime number.")

#             break

#     else:

#         print(f"{number} is a prime number.")

# else:

#     print("Please enter a value above 1")


number = int(input("Enter a number: "))

while(number <= 1):

    print("Please enter a value above 1")

    number = int(input("Enter a number again: "))

for i in range(2,number):

    if number % i == 0:

        print(f"{number} is not a prime number.")

        break

else:

    print(f"{number} is a prime number.")