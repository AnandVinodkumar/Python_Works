#define a function to find largest of 3 nos

def largest(num1,num2,num3):

    """
    if num1 >= num2 and num1 >= num3:

        print(f"{num1} is largest.")

    elif num2 >= num1 and num2 >= num3:

        print(f"{num2} is largest.")

    elif num3 >= num1 and num3 >= num2:

        print(f"{num3} is largest")
    """
    print(max(num1,num2,num3))

largest(1,2,3)