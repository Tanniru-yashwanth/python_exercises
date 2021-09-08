"""1. Write a function that takes a list as a parameter and returns the number of items in the list. Do NOT use the built-in len()
    or count() function."""


def num_items(lst):
    a = 0
    for i in lst:
        a += 1
    return a


lst_1 = []
print(num_items(lst_1))
