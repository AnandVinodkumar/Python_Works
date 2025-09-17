number = [1,3,5,2,4,5,6]  #Remove odd nos. from list

"""
for i in number:

    if i % 2 != 0:

        number.remove(i)

print(number)   #[3,4,2,6]
"""

for i in number.copy():

    if i % 2 != 0:

        number.remove(i)

print(number)   #[2,4,6]