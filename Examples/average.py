from functools import reduce

numbers = [2,3,4,5,6]

sum = reduce(lambda a,b : a + b, numbers)

print(f"Average = {sum/len(numbers)}")