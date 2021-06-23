string_ = input("Enter the string: ")
sub_string_ = input("Enter the sub string: ")


def count_string_sub_string(string, sub_string):
    lss = len(sub_string)
    ls = len(string)
    list_1 = []
    count = 0
    for i in range(0, ls):
        a = string[i:i + lss]
        list_1.append(a)
    for x in list_1:
        if x == sub_string:
            count += 1
    return count


print(count_string_sub_string(string_, sub_string_))