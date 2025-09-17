num1 = int(input("Enter the first number: "))

num2 = int(input("Enter the second number: "))

factor1 = [i for i in range(1,num1 + 1) if num1 % i == 0]

factor2 = [i for i in range(1,num2 + 1) if num2 % i == 0]

print(f"The GCD of {num1} and {num2} is {max(set(factor1).intersection(set(factor2)))}")