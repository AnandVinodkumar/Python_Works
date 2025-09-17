string1 = "Hello World! This is a test string."

for i in string1:
    
    if i.islower():
        
        print(i.upper(), end="")

    else:

        print(i, end="")