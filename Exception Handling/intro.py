# Error
"""
num = 10

if num > 0  # SyntaxError: expected ':'

    print("Positive")
"""

# Exception
# try, except
"""
Handles errors that occur during the execution of program
"""

# try: Contains the code which may get the exception
# except: Used to handle exceptions without breaking the execution

"""
num1 = int(input("Enter first number: "))

num2 = int(input("Enter second number: "))

try:

    print(num1/num2)

except:

    print("Division by Zero is not possible!")

print("Thank you")
"""
"""
numbers = [1,2,3]

try:

    index = int(input("Enter the number: "))

    print(numbers[index])

except IndexError:

    print("Enter a valid index.")

except ValueError:

    print("Enter an integer index.")

print("Thank you")
"""
#raise: used to raise the exception in between execution to stop the execution
#=====================================================================================

try:

    marks = int(input("Enter your marks: "))

    if marks < 0 or marks > 100:

        raise ValueError    # Raise an exception if conditionis met
                            # and execution jumps to exception block
    
    if marks > 60:

        print("Passed")

    else:

        print("Failed")

except ValueError:

    print("Enter a valid mark.")

# Ask the user to input a string and an integer for index
# Print the substring from index to end in reverse
# handle
# index error
# value error

try:

    string1 = input("Enter a string: ")

    index = int(input("Enter an index: "))

    for i in string1:

        if string1[index] == i:

            print(string1[index:][::-1])

except IndexError:

    print("Enter a valid index.")

except ValueError:

    print("Enter an integer index.")