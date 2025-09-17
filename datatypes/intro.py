# #Datatypes
# #======================

# #int  >>  +ve, -ve, 0

# #str  >>  any characters, digits, special characters, whitespaces within quotes considered as a string
#              # "hello 123"  >>  string (Collection of characters)

# name = "he12345llo"  #string    collection of characters

# age = 25  #int       #int datatype  >>  a positive (well defined) value

# height = 5.8  #float    #if the value is a decimal number, it is a float datatype

# is_allowed = True  

# subject = "python"

# print(subject[3]) # Output: h

# print(subject[2]) # Output: t

# print(subject[19]) # Output: IndexError: string index out of range

#p y t h o n
#0 1 2 3 4 5

# Advantages of index positioning
#==================================
# Always starts from 0

# Can fetch a specific element from a string

# name1="hello"

# name2="world"

# print(name1 + name2)  # Output: helloworld (concatenation of two strings)

# print(name1 + 2)  # Output: TypeError: can only concatenate str (not "int") to str

# position = "Fullstack Web Developer"

# #slicing
# print(position[0])  # Output: F

# print(position[-1])  # Output: r (negative index starts from the end of the string)

# print(position[0:9])  # Output: Fullstack (slicing from index 0 to 8)

# # Web Dev
# print(position[10:17])  # Output: Web Dev (slicing from index 10 to 16)

# #Web Developer
# print(position[10:])  # Output: Web Developer (slicing from index 10 to 22)

# #Reverse the entire string
# print(position[::-1])  # Output: repoleveD beW kcatstluF (reverses the string)

#Output and Input Functions
#==================================

# print("Hello World")  # Output: Hello World

# name = input()

# print(f"Hello {name}")  # Output: Hello followed by the name entered by the user

"""

# num1 = input("Enter first number: ")  # Input: 10

# num2 = input("Enter second number: ")  # Input: 20

# print(num1 + num2)  # Output: 1020 (concatenation of two strings)

"""

# num1 = int(input("Enter first number: "))  # Input: 10

# num2 = int(input("Enter second number: "))  # Input: 20

# print(num1 + num2)  # Output: 30 (addition of two integers)

# int() >> converts only the digits in a string to an integer



#Methods    To Manipulate, count, and modify strings
#==================================

name = "hello"

print(name.capitalize())  # Output: Hello (capitalizes the first letter)

print(name.upper())  # Output: HELLO (converts all characters to uppercase)

print(name.lower())  # Output: hello (converts all characters to lowercase)

print(name.count("l"))  # Output: 2 (counts the occurrences of 'l')

print(name.find("l"))  # Output: 2 (finds the index of the first occurrence of 'l')

print(name.index("l"))  # Output: 2 (finds the index of the first occurrence of 'l')

"""
isdigit() >> checks if all characters in the string are digits

isalpha() >> checks if all characters in the string are alphabetic

isalnum() >> checks if all characters in the string are alphanumeric (digits and letters)
"""