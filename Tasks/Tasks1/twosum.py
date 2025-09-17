list1 = [1,2,3,4,5,6,7,8,9,10]

target = int(input("To what sum should the pairs add up to?: "))

print("The pairs are: ")

for i in range(len(list1)):

    for j in range(i+1,len(list1)):

        if list1[i] + list1[j] == target:

            print(f"{list1[i]},{list1[j]}")