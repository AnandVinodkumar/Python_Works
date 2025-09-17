name = input("Enter a word: ")

count = name.count(name[0])

freq = name[0]

for i in range(1,len(name)):

    if name.count(name[i]) > count:

        count = name.count(name[i])

        freq = name[i]

print(f"The most frequent character in {name} is {freq}.")