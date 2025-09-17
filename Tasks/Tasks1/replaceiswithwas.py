string1 = "This is a test string."

list1 = string1.split(" ")

for i in list1:

    if i != "is":

        print(i, end=" ")

    else:

        print("was", end=" ")