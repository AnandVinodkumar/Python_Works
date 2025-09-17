string1 = input("Enter first string: ")

string2 = input("Enter second string: ")

if len(string1) != len(string2):

    print("The strings are not anagrams.")

else:

    for i in string1:

        if i not in string2:

            print("The strings are not anagrams.")

            break
    else:

        print("The strings are anagrams.")