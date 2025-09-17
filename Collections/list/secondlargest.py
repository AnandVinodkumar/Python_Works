numbers = [57,57,-57,57]

#WAP to find the second largest without max() function

numbers.sort(reverse=True)

largest = numbers[0]

second_largest = 0

for i in numbers:
    
    if i < largest:

        second_largest = i

        break
        
print(f"The second largest element is {second_largest}")