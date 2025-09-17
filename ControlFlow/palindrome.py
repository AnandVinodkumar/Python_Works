#WAP to check if a string is a palindrome or not

name = input("Enter a string: ")

if name.lower() == name[::-1].lower():
    
    print(f"{name} is a palindrome.")

else:

    print(f"{name} is not a palindrome.")