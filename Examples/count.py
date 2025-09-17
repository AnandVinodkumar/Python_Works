#Return the count of digits in a string

name = "qwerty@1234"

i = 0

count = 0

while(i < len(name)):

    if name[i].isdigit():

        count += 1

    i += 1

print(f"The count of digits in string is {count}")