def second_largest(list1):

    list1.sort(reverse=True)

    largest = list1[0]

    for i in list1:

        if i != largest:

            return i

print(f"The second largest element is {second_largest([1,2,3,4,5,6,7,8,9,10])}")