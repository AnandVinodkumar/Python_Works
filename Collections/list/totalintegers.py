items = [1,True,"hello","python",3,5,4]

count = 0

for i in items:

    # if str(i).isdigit():

    #     count += 1

    if type(i) == int:

        count += 1

print(f"The total no. of integer elements is {count}")  #4