marks = int(input("Enter the marks obtained: "))

if marks < 0 or marks > 100:

        print("Invalid Marks")

elif marks > 90:

    print("Grade: A")

elif marks >= 81 and marks <= 90:
    
    print("Grade: B")

elif marks >= 71 and marks <= 80:
    
    print("Grade: C")

elif marks >= 50 and marks <= 70:
    
    print("Grade: D")

else:

    print("Failed")