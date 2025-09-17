string1 = "Hello World! This is a test string."

string2 = "aeiou"

count = 0

for i in string1.lower():

    if i in string2:

        count += 1

print(f"The number of vowels in the string is {count}")