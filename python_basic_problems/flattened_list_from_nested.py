# Python Program to Make a Flattened List from Nested List

nested_list = [1, 2, 3, 4, [7, 8, 9]]
final_list = []
for x in nested_list:
    if type(x) == type([]):
        for i in x:
            final_list.append(i)
    else:
        final_list.append(x)
print(final_list)
