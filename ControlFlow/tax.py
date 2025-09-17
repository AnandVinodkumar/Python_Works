"""
Ask the user to enter price of a bike
if the price is greater than 100000, add 12% tax
if the price is greater than 50000 but less than or equal to 100000, add 7% tax
if the price is less than or equal to 50000, add 5% tax
"""
price_bike = int(input("Enter the price of the bike: "))

if price_bike > 100000:

    print(f"The price after tax is: {price_bike + (price_bike * 0.12)}")

elif price_bike > 50000 and price_bike <= 100000:

    print(f"The price after tax is: {price_bike + (price_bike * 0.07)}")

else:

    print(f"The price after tax is: {price_bike + (price_bike * 0.05)}")