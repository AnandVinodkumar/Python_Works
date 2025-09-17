def count_vowels(s):

    vowels = "aeiou"

    count = 0

    for i in s.lower():

        if i in vowels:

            count +=1
    
    return count

string1 = input("Enter a string: ")

print(f"The no of vowels in the string is {count_vowels(string1)}")