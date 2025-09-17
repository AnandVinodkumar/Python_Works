# # name = "afsal"  #Afsal without capitalizing
# # # print(name.capitalize())

# # # name[0]   # Output: a (first character in lowercase)

# # # name[0].upper()  # Output: A (first character in uppercase)

# # # name[1:]  # Output: fsal (rest of the string in lowercase)

# # print(name[0].upper() + name[1:])  # Output: Afsal (capitalizes the first letter manually)

# # name = "amal"  #Amal without capitalizing

# # name[-1]  # Output: l (last character in lowercase)

# # name[-1].upper()  # Output: L (last character in uppercase)

# # name[:3]  # Output: ama (first three characters in lowercase)

# # print(name[:3] + name[-1].upper())  # Output: amaL (capitalizes the last letter manually)

# name = "python"  #nythop

# # name[-1]  # Output: n (last character)

# # name[1:5]  # Output: ytho (middle characters)

# # name[0]  # Output: p (first character)

# print(name[-1] + name[1:5] + name[0])  # Output: nythop (last character + middle characters + first character)

# name = "madam"  #Print True if the string is a palindrome

# print(name == name[::-1])  # Output: True (checks if the string is a palindrome)


# Get the marks of subject1, subject2, and subject3 from the user
# Calculate total sum
# Calculate average

marks1 = int(input("Enter marks for subject 1: "))

marks2 = int(input("Enter marks for subject 2: "))

marks3 = int(input("Enter marks for subject 3: "))

total = marks1 + marks2 + marks3

average = total / 3

print(total)

print(average)