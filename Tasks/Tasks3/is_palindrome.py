def is_palindrome(s):

    if s == s[::-1]:

        return True
    
    else:

        return False

string1 = input("Enter a string: ")

if is_palindrome(string1):

    print(f"{string1} is a paindrome.")

else:

    print(f"{string1} is not a paindrome.")