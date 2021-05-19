"""Write a Python program to compute the sum of elements of a given array of integers, use map() function"""

array_1 = {23, 45, 67, 98, 76, 567, 897, 908767}


def sum_1(arr):
    add = 0
    for i in arr:
        add = i + add
    return add


print(list(map(sum_1, array_1)))


