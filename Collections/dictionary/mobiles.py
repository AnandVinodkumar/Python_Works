mobiles = {
    "Apple" : {"model" : "iphone16", "price" : 100000, "color" : "Black"},
    "Samsung" : {"model" : "s24", "price" : 115000, "color" : "Grey"},
    "OnePlus" : {"model" : "9r", "price" : 90000, "color" : "White"},
    "Google" : {"model" : "pixel", "price" : 120000, "color" : "Black"}
}

# List all the brand names
print("Brand names")

print()

for i in mobiles:

    print(i)

print("========================")

# List of values of all elements
print("All values")

print()

for i in mobiles:

    print(mobiles[i])

print("========================")

# List all the model names
print("All models")

print()

for i in mobiles:

    print(mobiles[i]["model"])

print("========================")

# List all the prices
print("All prices")

print()

for i in mobiles:

    print(mobiles[i]["price"])

print("=======================")

# List all model name along with price
print("All model names along with price")

print()

for i in mobiles:

    print(f"{mobiles[i]["model"]}  {mobiles[i]["price"]}")

print("=========================")

# List all model names which are above 1 lakh
print("Model names above 1 lakh")

print()

for i in mobiles:

    if mobiles[i]["price"] > 100000:

        print(f"{i} {mobiles[i]["model"]}")

print("=========================")

# List all model names between 1lakh and 1.5lakh
print("All model names between 1lakh and 1.5lakh")

print()

for i in mobiles:

    if mobiles[i]["price"] > 100000 and mobiles[i]["price"] < 150000:

        print(f"{i} {mobiles[i]["model"]}")

print("===============================")

# List model name which has black in color and price above 1lakh
print("Model name which has black in color and price above 1lakh")

print()

for i in mobiles:

    if mobiles[i]["color"] == "Black" and mobiles[i]["price"] > 100000:

        print(f"{i} {mobiles[i]["model"]}")

print("==================================")

# List model name along with brand name which has either black in color or price above 110000
print("Model name along with brand name which has either black in color or price above 110000")

print()

for i in mobiles:

    if mobiles[i]["color"] == "Black" or mobiles[i]["price"] > 110000:

        print(f"{i} {mobiles[i]["model"]}")

print("====================================")

# List the name which is between 1lakh and 1.5lakh and color should not be Black
print("The name which is between 1lakh and 1.5lakh and color should not be Black")

print()

for i in mobiles:

    if mobiles[i]["color"] != "Black" and mobiles[i]["price"] > 100000 and mobiles[i]["price"] < 150000:

        print(f"{i} {mobiles[i]["model"]}")

print("====================================")

