string1 = "Hello World! This is a test string."

list1 = string1.split(" ")

longest_word = ""

for i in list1:

    if len(i) > len(longest_word):
        
        longest_word = i

print(f"The longest word in the string is {longest_word}")