number = input("Enter a number: ")

new = ""

for i in number:

    if i not in new:

        if int(i) % 2 == 0:

            new += i

            print(f"Count of {i}: {number.count(i)}")