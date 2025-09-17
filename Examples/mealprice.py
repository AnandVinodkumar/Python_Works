cost = int(input("Enter the cost of the meal: "))

tip = 18 * cost / 100

tax = 5 * cost / 100

bill_amount = cost + tip + tax

print(f"Tip given: {tip:.2f}\nTax Issued: {tax:.2f}\nTotal cost: {bill_amount:.2f}")