# Collections

# Sets  No Index 

"""
elements = {"hello","python","language","hello"}    # Elements enclosed in Curly Brackets {}

# for i in range(5):

#     print(elements) # Does not maintain order when run multiple times and avoids duplicates

elements.add("bye") # Mutable

elements.add("python")  # No change

print(elements.pop())   # Removes a random element

elements.remove()   #Removes element if present
"""

items1 = {"1",1,"python",2,3,4,5}

items2 = {"language",1,2,3} # Union, Intersection, Difference

items3 = items1.union(items2)

print(items3)   #{1, 2, 3, 4, 5, '1', 'python', 'language'}

items4 = items1.intersection(items2)

print(items4)   #{1,2,3}

items5 = items1.difference(items2)

print(items5)   #{'1', 4, 5, 'python'}


