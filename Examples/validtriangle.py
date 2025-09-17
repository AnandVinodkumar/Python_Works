side1 = int(input("Enter the largest side of triangle: "))

side2 = int(input("Enter the second side: "))

side3 = int(input("Enter the third side: "))

if side2 + side3 > side1:

    print("These sides can form a triangle.")

    if side1 == side2 and side2 == side3:

        print("Equilateral")

    elif side1 == side2 or side2 == side3 or side1 == side3:

        print("Isocelos")

    else:

        print("Scalene")

else:

    print("These sides cannot form a triangle.")