name = input("Enter a string: ")

new = ""

for i in name:

    if i == " ":

        new += " "

    elif i.isalnum() == True:

        new += i

print(f"After removing special characters: {new}")