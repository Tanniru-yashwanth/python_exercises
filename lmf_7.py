""" Write a Python program to add two given lists and find the difference between lists. Use map() function. """

list_1 = [1, 3, 56, 76, 897, 567]
list_2 = [23, 65, 76, 87, 990]


def add_diff(x, y):
    a = x + y
    b = x - y
    return a, b


print(list(map(add_diff, list_1, list_2)))
