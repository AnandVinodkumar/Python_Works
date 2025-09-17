name = "A man, a plan, a canal - Panama"

new = ""

for i in name:

    if i.isalpha():
        
        new += i.lower()

print(new)

if new == new[::-1]:

    print("Palindrome")

else:

    print("Not palindrome")