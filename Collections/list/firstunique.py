numbers = [1,3,4,1,3,2,2]

print("The first unique element is: ",end="")

for i in numbers:

    if numbers.count(i) == 1:

        print(i)

        break
