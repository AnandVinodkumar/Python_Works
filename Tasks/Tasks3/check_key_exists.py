def check_key(**kwargs):

    if "age" in kwargs:

        print("The key age exists.")
        
    else:

        print("The key age does not exist")

check_key(name="Anand",place="Kochi",age=21)