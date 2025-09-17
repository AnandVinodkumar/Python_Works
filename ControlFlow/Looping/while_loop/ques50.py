num = int(input("Enter a number between 10 and 20: "))

while(num < 10 or num > 20):
    if num < 10:

        print("Too Low")

    elif num > 20:

        print("Too high")

    num = int(input("Enter a number between 10 and 20: "))

print("Thank You")