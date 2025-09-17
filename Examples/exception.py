number = int(input("Enter a number: "))
try:
    
    if type(number) is not int:
        
        raise TypeError
    
    elif number < 0:
        
        raise ValueError
    
except TypeError:

    print("ValueError: Enter an integer.")

except ValueError:

    print("NegativeNumberError: Enter a positive integer.")