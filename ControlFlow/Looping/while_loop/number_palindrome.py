"""
number = 121

temp = str(number)

if temp[::-1] == temp:

    print("The number is a palindrome.")

else:

    print("The number is not a palindrome.")
"""

number = int(input("Enter a number: "))

temp = number

reversed_num = 0

while(temp > 0):

    digit = temp % 10

    reversed_num = reversed_num * 10 + digit

    temp //= 10

if reversed_num == number:

    print(f"{number} is a palindrome")

else:

    print(f"{number} is not a palindrome")