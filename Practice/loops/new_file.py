
def max_list(list_1):
    if list_1:
        maxi = list_1[0]
        for x in list_1:
            if x > maxi:
                maxi = x
        return maxi
    else:
        return "Given list is empty"


list_1 = [-1, -2]
print(max_list(list_1))
