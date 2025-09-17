string1 = "AABBCDAB"

freq = 0

ele = ""

string2 = ""
for i in string1:

    if string1.count(i) > 1:

        print(f"The first recursive character is {i}")

        break

for i in string1:
    
    if i not in ele:
    
        if string1.count(i) > 1:

            print(i,"=", string1.count(i),end=" ")

            ele += i

print()

for i in string1:

    if string1.count(i) == 1:

        print(f"The first non-recursive character is {i}")

        break
ele1 = ""

for i in string1:

    if string1.count(i) >= freq:

        freq = string1.count(i)

        print(f"{i}")

        ele += i

        if i not in string2:

            string2 += i*freq

print(string2)