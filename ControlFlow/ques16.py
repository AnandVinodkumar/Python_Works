is_rainy = input("Is it raining? (yes/no): ")

is_rainy = is_rainy.lower()

if is_rainy == "yes":

    is_windy = input("Is it windy? (yes/no): ")

    is_windy = is_windy.lower()

    if is_windy == "yes":
        
        print("It is too windy for an umbrella.")

    else:

        print("Take an umbrella.")

else:

    print("Enjoy your day.")