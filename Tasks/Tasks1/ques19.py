student_name = input("Enter your name: ")

student_marks = int(input("Enter your marks: "))

student_grade = ""

if student_marks >= 91:

    student_grade = "A"

elif student_marks >= 81:

    student_grade = "B"

elif student_marks >= 71:

    student_grade = "C"

elif student_marks >= 61:

    student_grade = "D"

else:

    student_grade = "Fail"

print(f"Student Name: {student_name}\nMarks: {student_marks}\nGrade: {student_grade}")