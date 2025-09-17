# Sum of numbers which are divisible by 5

numbers = [1,3,2,4,5,6,10,15]

print(sum(list(filter(lambda a : a % 5 == 0,numbers))))