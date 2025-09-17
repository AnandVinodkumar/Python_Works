# Jumping Statements
#==============================

# Keywords used to alter the flow of the loop

# break
"""
for i in range(100):

    print(i)

    if i == 20:
    
        break   #Used to break the execution and exit from a loop
"""

# continue
"""
for i in range(10):

    if i % 2 == 0:

        continue     #Used to skip the specific loop (if the condition is met)

    print(i)
"""

#name = "python"    o/p->"pto"

name = "python"

new = ""

for i in range(0,len(name),2):

    if i % 2 != 0:

        continue

    new += name[i]

print(new)