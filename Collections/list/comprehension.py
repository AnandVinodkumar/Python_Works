# List Comprehension
#============================

numbers = [4,2,3,54,6,6,3,2,1,4,5,7,15,30,45]

odd = [i for i in numbers if i % 2 != 0]

print(odd)

# print even nos in a list

even = [i for i in numbers if i % 2 == 0]

print(even)

# print nos divisible by 3 and 5

divis = [i for i in numbers if i % 3 == 0 and i % 5 == 0]

print(divis)

# print unique elements in a list

unique = [i for i in numbers if numbers.count(i) == 1]

print(unique)