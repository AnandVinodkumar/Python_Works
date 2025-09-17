file1 = open("file1.txt","a")

file1.write("Hello World")

file1.write("\n")

file1.write("Welcome to Python Programming")

file1.write("\n")

file1.close()

# Remove duplicate lines

file1 = open("file1.txt","r")

lines = file1.readlines()

file1.close()

lines_set = set(lines)

file1 = open("file1.txt","w")

for line in lines_set:

    file1.write(line)

file1.close()
