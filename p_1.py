"""Python program to interchange first and last elements in a list"""


def swap_list(a):
    a[0], a[len(a) - 1] = a[len(a) - 1], a[0]
    return a


b = [1, 2, 4, 5, 6]
print(swap_list(b))

