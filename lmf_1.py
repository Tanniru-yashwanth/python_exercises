"""Write a python program to triple all numbers of a given list of integers.Use python map. """

numbers = [2, 3, 4, 5, 6, 7, 8, 9, 66]


def triple(x):
    a = x * x * x
    return a


print(list(map(triple, numbers)))
