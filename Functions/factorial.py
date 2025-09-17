"""
def factorial(n):

    if n == 0 or n == 1:

        return 1

    else:
        
        fact = 1

        for i in range(1,n+1):

            fact *= i
        
        return fact
    
n = int(input("Enter a number: "))

print(factorial(n))
"""

# Recursive Function
#============================
def factorial(a):

    if a == 0 or a == 1:

        return 1
    
    else:

        return a * factorial(a-1)   # 4 * factorial(3)
                                    #         3 * factorial(2)
                                    #                 2 * factorial(1)
                                    #                         1
    
a = int(input("Enter a number: "))

while(a < 0):

    print("Enter a positive integer: ")

    a = int(input("Enter another number: "))

print(f"Factorial of {a} is {factorial(a)}")