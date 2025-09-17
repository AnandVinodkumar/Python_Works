fruits = ["apple","banana","grape","cherry"]

vowels = "aeiou"

d = {}
# {'apple': 2, 'banana': 3, 'grape': 2, 'cherry': 1}

for i in fruits:

    count = 0   # Resetting the count variable after each element in dictionary

    for j in i:

        if j in vowels:

            count += 1

        d[i] = count

print(d)