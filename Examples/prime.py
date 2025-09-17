n = int(input("Enter a number: "))

i = 2

flag = 0

while(i <= n // 2):

    if n % i == 0:

        flag = 1

        break

    i += 1

if flag == 1:

    print(f"{n} is not a prime number.")

else:

    print(f"{n} is a prime number.")