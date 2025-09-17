#(1) Sum of first 15 natural numbers
"""
i = 0

sum = 0

while(i <= 15):

    sum += i
    
    i += 1

print(f"Sum of first 15 natural numbers is {sum}")
"""

#(2) Count number of digits in a number
"""
number = int(input("Enter a number: "))

temp = number

digit = 0

while(temp > 0):

    rem = temp % 10

    temp = temp // 10

    digit += 1

print(f"Number of digits in {number} is {digit}")
"""

#(3) Check whether a number is a palindrome
"""
number = int(input("Enter a number: "))

reversed_num = 0

length = len(str(number))

temp = number

while(temp > 0):

    digit = temp % 10   

    reversed_num += digit * (10 ** (length -1))  

    temp = temp // 10

    length -= 1

if reversed_num == number:

    print("Palindrome")

else:

    print("Not Palindrome")
"""

#(4) Extract digits from a string and sum of all digits
"""
string1 = "qwerty1234!@#$%^6789ZXCV"

i = 0

sum = 0

while(i < len(string1)):

    if string1[i].isdigit():

        sum += int(string1[i])

    i += 1

print("The sum of digits is",sum)
"""

#(5) Sum of all multiples of 3 or 5 below 1000
"""
i = 1

sum = 0

while(i < 1000):

    if i % 3 == 0 or i % 5 == 0:

        sum += i
    
    i += 1

print(f"The sum is {sum}")
"""

#(6) while loop until 'exit'
"""
user_input = ""
while(user_input!='exit'):

    user_input = input("Enter any input.(Enter 'exit' to end the code): ")
"""

#(7) LCM using while loop
"""
num1 = int(input("Enter the first number: "))

num2 = int(input("Enter the second number: "))

if nn
"""

#(9) Capitalize every 3rd char in a string
"""
name = input("Enter a string: ")

new = ""

length = len(name)

i = 0

while(i < length):

    if i % 3 == 2:

        new += name[i].upper()

    else:

        new += name[i]

    i += 1

print(new)
"""

#(10) Strong number
"""
number = int(input("Enter a number: "))

temp = number

fact = 1

new = 0

while(temp > 0):

    digit = temp % 10

    while(digit > 0):

        fact *= digit

        digit -= 1

    new += fact

    temp = temp // 10

    fact = 1

if new == number:

    print(f"{number} is a strong number")

else:

    print(f"{number} is not a strong number.")
"""

#(11) No. of odd and even nos
"""
name = "qwe342rty6547"

evencount = 0

oddcount = 0

i = 0

while(i < len(name)):

    if name[i].isdigit():

        if int(name[i]) % 2 == 0:

            evencount += 1
        
        else:

            oddcount += 1

    i += 1

print(f"Oddcount = {oddcount}")

print(f"Evencount = {evencount}")
"""