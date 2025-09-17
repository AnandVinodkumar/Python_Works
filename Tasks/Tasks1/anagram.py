name1 = input("Enter first word: ")

name2 = input("Enter second word: ")

name1 = name1.lower()

name2 = name2.lower()

if len(name1) == len(name2):

    for i in name1:

        if i not in name2:

            print(f"{name1} and {name2} are not anagrams of each other.")

            break
    else:

        print(f"{name1} and {name2} are anagrams of each other.")

else:

    print(f"{name1} and {name2} are not anagrams of each other.")

