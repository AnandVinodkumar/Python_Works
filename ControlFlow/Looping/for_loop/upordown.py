choice = input("Do you want to count up or down?: ")

if choice.lower() == "up":

    number = int(input("Enter a number: "))

    for i in range(1,number+1):

        print(i)

elif choice.lower() == "down":

    number = int(input("Enter a number below 20: "))

    if number >= 20:

        print("Dude Listen To Me!!!!!!!!!")

    else:
        for i in range(20,number-1,-1):

            print(i)

else:

    print("I dont understand")