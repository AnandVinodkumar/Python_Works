grocery = {
    "apple" : 50,
    "banana" : 20,
    "milk" : 30,
    "bread" : 25,
    "eggs" : 6
}

print(f"Available Items:")

for i in grocery:

    print(i,grocery[i])

cart = {}

choice = ""

while(choice.lower() != "done"):

    product = input("Enter the product: ")

    if product.lower() in grocery:

        quantity = int(input("How much do you want?: "))

        if product.lower() in cart:

            cart[product.lower()] += quantity

        else:

            cart[product.lower()] = quantity
    
    else:

        print("Sorry. Item not available.")

    choice = input("Please enter DONE if you are done. Press ENTER otherwise: ")
    
price = 0

for i in cart:

    price += (cart[i]*grocery[i])

print(f"Total price = {price}")