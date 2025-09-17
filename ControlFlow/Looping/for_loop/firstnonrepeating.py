#First Non-Repeating character
"""
name = "aabbcddef"

for i in name:

    if name.count(i) == 1:

        print(i)

        break
"""

#Second Non-Repeating character
"""
name = "aabbcddef"

count = 0

for i in name:

    if name.count(i) == 1:

        count += 1

        if count == 2:

            print(i)

            break
"""