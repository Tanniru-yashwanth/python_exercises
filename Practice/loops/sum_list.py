"""4. Write a function that takes a list of integers as a parameter and
returns the sum of the list. Do NOT use the built-in
    sum() function."""


def sum_lst(lst_1):
    maxi = 0
    for i in lst_1:
        maxi = maxi + i
    return maxi


lst = [23, 34, 67, 89]
print(sum_lst(lst))
