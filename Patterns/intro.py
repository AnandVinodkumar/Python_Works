# Patterns
#=====================

# for loop range(5)

"""
for i in range(5):

    print(i,end="")

print()

# *******

for i in range(7):

    print("*",end="")

print()

# $$$$$

for i in range(5):

    print("$",end="")

print()

# 111111

for i in range(6):

    print("1",end="")

print()
"""

"""
******
******
"""

# rows = 2

# for i in range(rows):

#     for j in range(6):

#         print("*",end="")

#     print()


"""
1111111
1111111
1111111
"""

# rows = 3

# for i in range(rows):

#     for j in range(7):

#         print(1,end="")

#     print()

"""
000000
111111
222222
333333
444444
"""
# rows = 5

# for i in range(5):

#     for j in range(6):

#         print(i,end="")

#     print()


"""
12345
12345
12345
12345
"""
# rows = 4

# for i in range(rows):

#     for j in range(1,6):

#         print(j,end="")

#     print()


"""
******
******
******
******
******
"""

# rows = 5

# for i in range(rows):

#     for j in range(6):

#         print("*",end="")

#     print()


"""
*
**
***
****
*****
"""

# rows = 5

# for i in range(rows):

#     print("*" * (i+1))


"""
* * * * *
* * * *
* * *
* *
*
"""
# rows = 5

# for i in range(rows,0,-1):

#     print("* " * (i))


"""
* * * * *
  * * * *
    * * *
      * *
        *
"""
"""
# rows = 5

# space = 0

# for i in range(rows,0,-1):

#     print(" " * (space),end="")

#     print("* " * i)

#     space += 2

"""

# rows = 5

# for i in range(rows):

#     print(i * "  " + "* " * (rows - i))


"""
    *
   * *
  * * *
 * * * *
* * * * *
"""

rows = 5

for i in range(1,rows):

    print((rows-i) * " " + "* " * (i) + " " * (rows-(i+1)))
