from functools import reduce

n = int(input("Enter a number: "))

list1 = []

for i in range(1,n+1):

    list1.append(i)

fact = 1

fact = reduce(lambda fact,a : fact * a, list1)

print(fact)