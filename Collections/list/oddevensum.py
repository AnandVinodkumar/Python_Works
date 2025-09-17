# numbers = [1,3,4,1,3,5,2,2]

# odd_sum = 0

# even_sum = 0

# for i in numbers:

#     if i % 2 == 0:

#         even_sum += i

#     else:

#         odd_sum += i

# print(f"Odd Sum = {odd_sum}\nEven Sum = {even_sum}")

"""
Print sum of elements in odd index position
"""

numbers = [1,3,4,1,3,5,2,2]

sum = 0

for i in range(0,len(numbers)):

    if i % 2 != 0:

        sum += numbers[i]

print(f"Sum of elements in odd index position is {sum}")    #11


"""
Print sum of elements in even index position 
"""

numbers = [1,3,4,1,3,5,2,2]

sum = 0

for i in range(0,len(numbers)):

    if i % 2 == 0:

        sum += numbers[i]

print(f"Sum of elements in even index position is {sum}")   #10
