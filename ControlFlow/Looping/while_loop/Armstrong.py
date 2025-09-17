"""
Armstrong number
A number that is the sum of its own digits each raised to the power of number of digits.
For example, 153    1^3 + 5^3 +3^3
"""

number = int(input("Enter a number: "))

length = len(str(number))

temp = number

sum = 0

while(temp > 0):

    sum += (temp % 10) ** length

    temp = temp // 10

    print(f"Sum = {sum}\nTemp = {temp}")

if sum == number:

    print(f"{number} is an Armstrong number.")

else:

    print(f"{number} is not an Armstrong number.")