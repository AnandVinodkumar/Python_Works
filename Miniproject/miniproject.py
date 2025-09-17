def armstrong(a):

    length = len(str(a))

    temp = a

    sum = 0

    while(temp > 0):

        sum += (temp % 10) ** length

        temp = temp // 10

    if sum == a:

        print(f"{a} is an Armstrong number.")

        print()

    else:

        print(f"{a} is not an Armstrong number.")

        print()

def prime(a):

    for i in range(2,a):

        if a % i == 0:

            print(f"{a} is not a prime number")

            break

    else:

        print(f"{a} is a prime number")
    
    print()

def spy(a):

    sum = 0

    prod = 1

    for i in str(a):

        sum += int(i)

        prod *= int(i)

    if sum == prod:

        print(f"{a} is a spy number.")

        print()

    else:

        print(f"{a} is not a spy number.")

        print()

def palindrome(a):

    temp = a

    reversed_num = 0

    while(temp > 0):

        digit = temp % 10

        reversed_num = reversed_num * 10 + digit

        temp //= 10

    if reversed_num == a:

        print(f"{a} is a palindrome")

        print()

    else:

        print(f"{a} is not a palindrome")

        print()

def perfect(a):

    sum = 0

    for i in range(1,a):

        if a % i == 0:

            sum += i

    if sum == a:

        print(f"{a} is a perfect number.")

        print()

    else:

        print(f"{a} is not a perfect number.")

        print()

def neon(a):

    new = a ** 2

    sum = 0

    for i in str(new):

        sum += int(i)

    if sum == a:

        print(f"{a} is a neon number.")

        print()

    else:

        print(f"{a} is not a neon number.")

        print()

client_name = input("Your Name?: ")

print()

print(f"Hello {client_name}! Welcome to the Special Number Finder!")
print("=====================================================================")

print()

print(f"Here you can enter a number and check whether that number is \n(i) An Armstrong number\n(ii) A Prime number\n(iii) A spy number\n(iv) A Palindrome number\n(v) A Perfect number\n(vi) A Neon number\n")

print()

print(f"Let's get started, shall we?")

print()

choice1 = "yes"

while(choice1.lower() == "y" or choice1.lower() == "yes"):

    choice = input("What do you want to find out?\n\nPlease enter the Roman Number of the option without brackets: ")

    print()

    while(choice.lower() == "(i)" or choice.lower().lower == "(ii)" or choice.lower() == "(iii)" or choice.lower() == "(iv)" or choice.lower() == "(v)" or choice.lower() == "(vi)"):

        print("Your choice should not contain any brackets")

        print("==============================================")

        choice = input("Please try again\n\nPlease enter the Roman Number of the option without brackets: ")

    while(choice.lower() != "i" and choice.lower() != "ii" and choice.lower() != "iii" and choice.lower() != "iv" and choice.lower() != "v" and choice.lower() != "vi"):

        print("Please enter a valid option.")

        print("==============================================")

        choice = input("Please enter the Roman Number of the option without brackets: ")

    if choice.lower() == "i":

        print("-------------------Armstrong Number------------------")

        number = int(input("Enter a number: "))

        armstrong(number)

    elif choice.lower() == "ii":

        print("-------------------Prime Number------------------")

        number = int(input("Enter a number: "))

        while(number <= 1):

            print("Please enter a value above 1")

            number = int(input("Enter a number again: "))

        prime(number)

    elif choice.lower() == "iii":

        print("-------------------Spy Number------------------")

        number = int(input("Enter a number: "))

        spy(number)

    elif choice.lower() == "iv":

        print("-------------------Palindrome Number------------------")

        number = int(input("Enter a number: "))

        palindrome(number)

    elif choice.lower() == "v":

        print("-------------------Perfect Number------------------")

        number = int(input("Enter a number: "))

        perfect(number)

    elif choice.lower() == "vi":

        print("-------------------Neon Number------------------")

        number = int(input("Enter a number: "))

        neon(number)

    choice1 = input("Do you want to check more?(yes/no): ")

print()

print("Thank you and have a nice day!")

print("==============================================")