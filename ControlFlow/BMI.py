# BMI Body Mass Index Calculator
"""
bmi = weight(kg) / height(m)^2
"""

weight = float(input("Enter your weight in kg: "))

height = float(input("Enter your height in meters: "))

bmi = weight / (height**2)

if bmi < 18.5:

    print(f"You are underweight.")

elif bmi >= 18.5 and bmi < 25:

    print(f"You have a normal weight.")

elif bmi >= 25 and bmi < 30:

    print(f"You are overweight.")

elif bmi >= 30 and bmi < 35:

    print(f"You are obese.")

else:

    print(f"You are extremely obese.")