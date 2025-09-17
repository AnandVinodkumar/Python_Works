# Collections

# Tuple ->  Immutable
"""
items = (1,2,3,4,5,1,2,3,4,5)    # Elements enclosed in Round Brackets ()

# methods -> count(), index()

for i in range(5):

    print(items)

items.count(1)  # returns count of element 1

items.index(1)  # returns index of first occurance of element 1

"""
items = ("Hello")

print(type(items))     # <class 'str'>

items = ("Hello",)

print(type(items))      # <class 'tuple'>

items1=()

for i in range(5):
    items1 = items1 + (i,)

print(items1)  # (0, 1, 2, 3, 4)