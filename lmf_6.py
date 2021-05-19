"""Write a Python program to convert all the characters in uppercase and lowercase and
eliminate duplicate letters from a given sequence. Use map() function."""

characters = {'a', 'B', 'N', 'l', 'p', 'a', 'p', 'G'}


def change_cases(s):
    a = s.upper(), s.lower()
    return a


print(list(map(change_cases, characters)))
