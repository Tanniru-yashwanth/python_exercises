# Python Program to Merge Two Dictionaries

dictionary_1 = {1: 'a', 2: 'b', 3: 'c', 4: 'd', 5: 'e'}
dictionary_2 = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}
for x in dictionary_2:
    dictionary_1[x] = dictionary_2[x]
print(dictionary_1)
