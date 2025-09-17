age = int(input("Enter your age: "))

while(age < 0):

    print(f"Invalid input")

    age = int(input("Enter a valid age: "))


if age >= 0 and age <= 12:

    print(f"You are a child.")

elif age >= 13 and age <= 19:

    print(f"You are a teen.")

elif age >= 20 and age <= 59:

    print(f"You are a adult.")

else:

    print(f"You are a senior.")