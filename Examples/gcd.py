def gcd(a, b):

    gcd_value = 1
    
    if a > b:

        for i in range(1, b + 1):

            if a % i == 0 and b % i == 0:

                gcd_value = i
    
    else:

        for i in range(1, a + 1):

            if a % i == 0 and b % i == 0:

                gcd_value = i
    
    return gcd_value

num1 = int(input("Enter first number: "))

num2 = int(input("Enter second number: "))

print(f"The GCD of {num1} and {num2} is {gcd(num1, num2)}")