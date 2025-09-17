"""
def square(n):

    return n**2

numbers = [2,3,4,5,6]

for i in numbers:

    print(f"Square of {i} = {square(i)}")
"""

# map() used to apply a function to all elements in an iterable

# map(function,iterable)    #<map object at 0x000001F14DB057B0>
"""
numbers = [2,3,4,5,6]

print(list(map(lambda n: n**2,numbers)))
"""

numbers = [2,3,4,5,6,7,8,9]

# Filtering process

# filter(function,iterable)

# Get all odd nos in list

print(list(filter(lambda i : i % 2 != 0, numbers)))   # Takes all elements that satisfy the condition in a list

# Get all even nos in list

print(list(filter(lambda i : i % 2 == 0, numbers)))

# Get all nos divisible by 3

print(list(filter(lambda i : i % 3 == 0, numbers)))


numbers = [2,3,4,5,6,7,8,9]

# Find sum of all numbers in the list

from functools import reduce

sum = reduce(lambda a,b : a + b, numbers)

"""
a = 0 (This is always the starting point)

b = each element from list

"""

print(sum)

# Find product of all numbers in the list

from functools import reduce

print(reduce(lambda a,b : a *b, numbers))


"""
# Add square of all elements into a list

# From squared list of numbers filter the even numbers

# From the list of even numbers find the total

"""

numbers = [1,3,2,4,6,7,8,9,4,11]

list1 = list(map(lambda i : i ** 2, numbers))

print(list1)

list2 = list(filter(lambda i : i % 2 == 0, list1))

print(list2)

print(reduce(lambda a,b: a + b, list2))

