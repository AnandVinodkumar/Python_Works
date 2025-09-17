def common_elements(list1,list2):

    list3 = []

    list3 = set(list1).intersection(set(list2))

    print(list(list3))

list1 = [1,2,3,4,5,6]

list2 = [4,5,6,7,8,9]

common_elements(list1,list2)

