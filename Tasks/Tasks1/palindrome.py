name = input("Enter a string: ")

if name.lower() == name[::-1].lower():
    
    print(f"{name} is a palindrome.")

else:

    print(f"{name} is not a palindrome.")