# invitee = input("Who do you want to invite to the party?: ")

# print(f"{invitee} has now been invited.")

# count = 1

# choice = input("Do you want to invite anyone else to the party?(yes/no): ")

# while(choice == 'yes'):

#     invitee = input("Who do you want to invite to the party?(yes/no): ")

#     print(f"{invitee} has now been invited.")

#     count += 1

#     choice = input("Do you want to invite anyone else?(yes/no): ")

# print(f"You invited {count} people to the party")


count = 0

i = 0

while(i <= 0):

    invitee = input("Who do you want to invite to the party?: ")

    print(f"{invitee} has now been invited.")

    count = 1
    
    choice = input("Do you want to invite anyone else to the party?(yes/no): ")

    if choice == 'n':

        i = 1

    else:
        i = 0

print(f"You invited {count} people to the party")