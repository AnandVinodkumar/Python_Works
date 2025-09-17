def count_words(sentence):

    list1 = sentence.split()

    return len(list1)

s = input("Enter a sentence: ")

print(f"The no of words in the sentence is {count_words(s)}")