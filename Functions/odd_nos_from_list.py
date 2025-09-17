# Return odd numbers from a list of 5 numbers

def odd_list(list1):

    for i in list1:

        if i % 2 != 0:

            print(i)

list1 = []

print("Enter 5 numbers: ")

for i in range(5):

    ele = int(input(f"Enter number {i+1}: "))

    list1.append(ele)

print("Odd numbers are: ")

odd_list(list1)