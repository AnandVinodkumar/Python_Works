"""
#Grocery = ["apple","orange","cherry","grape"]

#User Input product

#Add to another cart if product in grocery and remove from grocery

#print sorry if product not in grocery

#Display total no of products in grocery
"""

Grocery = ["apple","orange","cherry","grape"]

cart = []

choice = input("Do you want any product?(yes/no): ")

while(choice.lower() == "yes"):

    product = input("Enter your product: ")

    if product in Grocery:

        Grocery.remove(product)

        cart.append(product)

    else:

        print("Sorry")

    print(len(Grocery))

    choice = input("Do you want any product?(yes/no): ")