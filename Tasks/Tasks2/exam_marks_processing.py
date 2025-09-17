marks = [45, 76, 88, 45, 90, 76]

print("76 appears",marks.count(76),"times in the list.")

marks.remove(45)

print(marks)

marks.append(100)

print(marks)

marks1 = marks.copy()

marks.sort(reverse=True)

print(marks)