string1 = "akajjshhhdhfyyyxdsak"

for i in string1:

    if string1.count(i) == 1:

        print("The first non-repeating character is:", i)

        break

else:

    print("There is no non-repeating character.")