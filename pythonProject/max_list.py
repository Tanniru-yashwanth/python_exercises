"""2. Write a function that takes a list of integers as a parameter and returns the max element in the list.
 Do NOT use the
    built-in max() function."""


def max_lst(lst):
    if lst_1:
        maxi = lst[0]
        for i in range(len(lst)):
            if lst[i] > maxi:
                maxi = lst[i]
        return maxi
    else:
        return "Given list is empty"


lst_1 = [-1, -2]
print(max_lst(lst_1))
