# Dictionary    items = {key:value}
"""
Datatype of KEY must be STRING or INTEGER

Datatype of VALUE can be whatever
"""

# [] list  () Tuple  {} dict

items = {}  # dictionary

# detail = ["python","kochi","Student"]

            #key     #value
items = {"language":"python","place":"kochi","role":"Student"}  #Dictionary is mutable

for i in items: # iterates over keys

    print(i)    # iterates only keys

    print(items[i])     # returns value

items["language"] = "Java"  # Updates a value

print(items)

# Add a new element
#=============================

# items[key] = value

items["is_available"] = True    # Adds a new element (key-value pair)

print(items)

