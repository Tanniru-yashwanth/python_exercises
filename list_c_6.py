"""Use a dictionary comprehension to count the length of each word in a sentence"""

sentence = "Use a dictionary comprehension to count the length of each word in a sentence"
words = sentence.split()
length = [len(x) for x in words]
dictionary = {w: l for (w, l) in zip(words, length)}
print(dictionary)
