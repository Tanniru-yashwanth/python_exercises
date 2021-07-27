# Python Program to Compute all the Permutation of the String
from itertools import permutations

string_input = input("Enter the string:")
length = len(string_input)


def fac(number):
    a = 1
    for i in range(1, number + 1):
        a = i * a
    return a


permutations_count = fac(length) // fac(length - length)

print(permutations_count)

permutations_get = permutations(string_input)
for x in permutations_get:
    print(x)
