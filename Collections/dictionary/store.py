store = {
    "apple" : 50,
    "banana" : 20,
    "milk" : 40,
    "bread" : 30
}

cart = {}

for i in store:

    print(i,store[i])

print()

choice = "yes"

while(choice.lower() == "yes" or choice.lower() == "y"):

    product = input("What do you want?: ")

    if product.lower() in store:

        quantity = int(input("How much do you need?: "))

        cart[product] = quantity
    
    else:

        print(f"Sorry, {product} not available")

        print()

    choice = input("Do you need anything else?(yes/no): ")

    print()

print(f"Your cart: {cart}")

print()

price = 0

for i in cart:

    price += cart[i]*store[i]

print()
print(f"Total bill amount = {price}")
