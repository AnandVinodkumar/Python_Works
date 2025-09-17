def is_prime(num):

    for i in range(2,num):

        if num % i == 0:

            print(f"{num} is not prime")

            break
    else:

        print(f"{num} is prime")

# num = int(input("Enter a number: "))

# while(num <= 1):

#     print("Invalid Input!!")

#     num = int(input("Enter a number: "))

# is_prime(num)