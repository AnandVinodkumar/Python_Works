name = "datascience"    #"a"  "c"  "e"      3

new = ""    #To insert duplicate elements

for i in name:

    if i not in new:    #To avoid counting an element twice

        if name.count(i) > 1:   #If a duplicate element is found, add to new

            new += i

print(f"There are {len(new)} duplicate elements")