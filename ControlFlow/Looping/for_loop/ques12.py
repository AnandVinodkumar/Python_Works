name = "aaabbccc"

new = ""

for i in name:

    if i not in new:

        n = name.count(i)

        new += i + str(n)

print(new)