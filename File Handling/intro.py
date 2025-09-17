# File Handling
#==================================
# Used to perform the below operation
# create new files
# read
# update
# delete

# read()    -   "r" >>  File should be existing
# write()   -   "w" >>  If file is existing, new content will override all the content in file, else creates the file
# append()  -   "a" >>  

# open()

"""
try:

    file = open(input("Enter a filename: "),"r")

    print(file.read())

except FileNotFoundError:

    print("Sorry, the requested file does not exist.")

print("Thank you")
"""

# Writing onto a file
#==================================

# write() "w"
"""
file = open("sample.txt","w")

file.write("Welcome Onam 2025")

file1 = open("Hello.txt","w")

file1.write("You just created a new file")
"""
# append()
# Used to add a content without overwriting
#=====================================================
"""
file = open("sample.txt","a")

file.write("\nHello World")
"""

# Ask user to input a word

# yes, count
"""
file = open("sample.txt","r")

data = file.read()

word = input("Enter the word: ")

if word in data:

    print(f"Yes \n{data.count(word)}")

else:

    print("No")
"""

# Create a file a.txt and write the content hello
# Create a file b.txt and write the content world
# Output in c.txt >> "hello world"

# file1 = open("a.txt","r+")

# file1.write("hello")

# file1.close()

# file2 = open("b.txt","w+")

# file2.write("world")

# file2.close()

# file3 = open("c.txt","w")

# file1 = open("a.txt","r")

# file2 = open("b.txt","r")

# file3.write(file1.read())

# file3.write(" ")

# file3.write(file2.read())

# file1.close()
# file2.close()
# file3.close()


file = open("C:/Users/Anand Vinodkumar/Desktop/Python Works/File Handling/aaa.txt","w")

file.write("hello")