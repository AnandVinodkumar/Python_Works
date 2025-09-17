marks = {"sub1":87,"sub2":55,"sub3":78,"sub4":98}

sum = 0

for i in marks:

    sum += marks[i]

avg = sum / len(marks)

print(f"Average of student's marks is {avg}")