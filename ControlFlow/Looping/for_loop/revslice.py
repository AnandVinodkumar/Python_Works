"""
name = "hellopython"

alphabet = "p"  ollehpython

alphabet = "z"  name[::-1]
"""

name = input("Enter a string: ")

alphabet = input("Enter an alphabet: ")

if alphabet in name:

    index = name.index(alphabet)

    print(name[0:index][::-1] + name[index:])

else:

    print(name[::-1])