num1 = int(input("Enter the number: "))

num2 = int(input("Enter the number: "))

sum = num1 + num2

choice = input("Do you want to add another number(y/n): ")

while(choice == 'y'):

    num3 = int(input("Enter the number: "))

    sum += num3

    choice = input("Do you want to add another number(y/n): ")

print(f"Total = {sum}")