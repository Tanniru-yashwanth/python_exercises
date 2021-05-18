"""Count the number of spaces in a string"""

sentence = "Count the number of spaces in a string"
spaces = [x for x in sentence if x == " "]
print(len(spaces))


