number = 50

num = int(input("Enter a number: "))

count = 1

while(num != number):

    if num < number:

        print("It's too low")

        num = int(input("Enter a number: "))

        count += 1

    elif num > number:

        print("It's too high")

        num = int(input("Enter a number: "))

        count += 1

print(f"Well done, you took {count} attempts")
