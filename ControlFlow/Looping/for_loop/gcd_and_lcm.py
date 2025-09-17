num1 = int(input("Enter a number: "))

num2 = int(input("Enter a number: "))

for i in range(1,num1 + 1):

    if num1 % i == 0 and num2 % i == 0:

        gcd = i

print(f"GCD is {gcd}")

lcm = (num1 * num2) / gcd

print(f"LCM is {lcm}")

 