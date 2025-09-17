# Lambda

"""
def square(n):

    return n ** 2

print(square(6))
"""

# Lambda is an anonymous function (nameless)

# One line functional statements

# Syntax:
# lambda arguments:expression

# lambda : keyword

# arguments : user input

# expression : return statement
"""
result  = lambda n: n ** 2

print(result(5))
"""

# Function to return cube of no.
"""
result1 = lambda n: n ** 3

print(result1(5))
"""

# Function to return square root of a number
"""
sqrt = lambda n: n**0.5

print(sqrt(4))
"""

# Function to return the last word of a sentence
"""
last_word = lambda text: text.split()[-1]

print(last_word(text="Python is a programming language"))
"""

# Function to return largest among 3 numbers
"""
largest = lambda a,b,c: max(a,b,c)

print(largest(10,3,8))
"""

# Function to return the no is even or odd
"""
odd_or_even = lambda n: "Odd" if n % 2 != 0 else "Even"

print(odd_or_even(5))
"""

# Function to return total no of vowels in a string
"""
vowels = lambda string1: len([i for i in string1 if i.lower() in "aeiou"])

print(vowels(string1="Hello There"))   #4
"""

# Function to return if no is positive, negative or zero

status = lambda n: "Positive" if n > 0 else ("Negative" if n < 0 else "Zero")

print(status(0))

