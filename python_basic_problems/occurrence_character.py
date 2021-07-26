# Python Program to Count the Number of Occurrence of a Character in String
from collections import Counter
string_input = list(input("Enter the string:"))
a = Counter(string_input)
for x in a:
    print(f" occurrence of {x} is {a[x]}")
