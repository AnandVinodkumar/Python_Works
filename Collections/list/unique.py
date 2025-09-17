numbers = [1,3,2,4,5,3,2]

print("The unique elements are: ",end="")

for i in numbers:

    if numbers.count(i) == 1:

        print(i,end=" ")