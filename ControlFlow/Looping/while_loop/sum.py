# WAP to find the sum of odd numbers between two numbers n1 and n2

n1 = int(input("Enter the first number: "))

n2 = int(input("Enter the second number: "))

sum = 0

while(n1 <= n2):

    if n1 % 2 != 0:
        
        sum += n1

    n1 += 1

print("Sum of odd numbers:", sum)