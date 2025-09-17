number = int(input("Enter a number: "))

temp = number

fact = 1

sum = 0

while(temp > 0):

    digit = temp % 10

    while(digit > 0):

        fact *= digit

        digit -= 1

    sum += fact

    temp = temp // 10

    fact = 1

if sum == number:

    print(f"{number} is a strong number")

else:

    print(f"{number} is not a strong number.")