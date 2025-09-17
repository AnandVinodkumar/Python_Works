# Modules
# ==================

# python file with variables and functions

# Reuse a piece of code instead of writing again and again


import data # This is a user-defined module

print(data.name)

for i in data.items:

    print(i,end=" ")

print()
# Built-in modules >> math, random



# Package
# =======================

# Directory which contains one or more modules

# Collection of modules

from Functions import prime

prime.is_prime(5)