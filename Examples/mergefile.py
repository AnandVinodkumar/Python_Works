file1 = open("file1.txt", "w")

file2 = open("file2.txt", "w")

file1.write("Hello World\n")

file2.write("Welcome to Python Programming\n")

file1.close()

file2.close()

file1 = open("file1.txt", "r")

file2 = open("file2.txt", "r")

file3 = open("file3.txt", "w")

for i in file1:

    file3.write(i)

for j in file2:

    file3.write(j)

file1.close()

file2.close()

file3.close()
