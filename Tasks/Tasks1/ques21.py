string1 = input("Enter a string: ")

for i in string1:
    
    if string1.count(i) == 1:

        print(f"The first character that appears only once is: {i}")

        break

else:

    print("No unique character found.")