# Python Program to Sort a Dictionary by Value

dictionary = {'a': 45, 'b': 54, 'c': 10, 'd': 4}
sorted_dict = sorted(dictionary.items(), key=lambda item: item[1])
print(dict(sorted_dict))
