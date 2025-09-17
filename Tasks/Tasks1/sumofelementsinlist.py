elements = []

for i in range(5):

    element = int(input(f"Enter the element: "))

    elements.append(element)

print(elements)

print(f"The sum of elements in the list is {sum(elements)}")