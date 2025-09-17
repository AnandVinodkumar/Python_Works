age = int(input("Enter your age: "))

if age < 0:

    print("Age cannot be negative.")

else:
    if age <= 16:

        print("You can go trick or treating.")

    elif age == 16:

        print("You can buy a lottery ticket.")

    elif age == 17:

        print("You can learn to drive.")

    else:

        print("You can vote.")