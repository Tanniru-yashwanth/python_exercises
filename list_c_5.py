"""Find all of the words in a string that are less than 5 letters"""

sentence = "Find all of the words in a string that are less than 5 letters"
txt = sentence.split()
sentence_1 = [words for words in txt if len(words) < 5]
print(sentence_1)


