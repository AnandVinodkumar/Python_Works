"""
input()
print()
len()
range()
sum()
max()
min()

built-in functions
"""
# Functions
#=======================

# A block of code which can be executed repeatedly when it is called

# code is reusable

def greet():    # Function header

    print("Hello Python!")  # Function body

greet() # Function caller

"""
Syntax:

def function_name():

    statements

function_name()

"""
"""
# def welcome():

#     print("Welcome 2026")

# welcome()
"""

"""
def welcome():

    return "Welcome 2026" # To exit the function's execution and send a value back to the caller.

print(welcome())
"""

# Sum of indefinite amount of numbers

# *args used to accept variable no. of arguments each time
#=========================================================
"""
def add(*args):
    
    print(args) #(10, 20, 30, 40)   As a tuple

    sum = 0

    for i in args:

        sum += i
    
    return sum

print(add(10,20,30,40))
"""

# *kwargs used to accept variable no. of keyword arguments each time
#=========================================================
def details(**kwargs):

    print(kwargs)   #{'name': 'Anand', 'place': 'Kochi'}    As a Dictionary

    pass

details(name = "Anand",place = "Kochi")