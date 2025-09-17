# Return a list of squared even numbers from the given list using a function

def square_even(elements):
    
    return [i**2 for i in elements if i % 2 == 0]

print(square_even([0,1,2,3,4,5,6,7,8,9,10]))