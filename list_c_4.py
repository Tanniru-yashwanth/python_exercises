"""Remove all the vowels in a string"""

sentence = "remove all the vowels in a string"
vowels = "aeiou"
sentence_1 = [x for x in sentence if x not in vowels]
print(sentence_1)


