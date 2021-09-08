"""3. Write a function that takes a list as a parameter and
returns the reversed list. Do NOT use the built-in reverse() function."""


def reverse_lst(lst):
    rev_lst = []
    a = -1
    for i in range(len(lst)):
        rev_lst.append(lst[a])
        a -= 1
    return rev_lst


lst_1 = [1, 2, 33, 78]
print(reverse_lst(lst_1))


def revers_lst(lst):
    for i in range(len(lst)):
        lst.insert(i, lst[len(lst) - 1])
        lst.pop(len(lst) - 1)
    return lst


lst_2 = [1, 2, 33, 78]
print(revers_lst(lst_2))
