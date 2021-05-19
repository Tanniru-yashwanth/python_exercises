"""Write a Python program to create a new list taking specific elements from a tuple
and convert a string value to integer"""

tuple_1 = ('s', '3', '56', '89', 'o', '990')

new_list = []
a = list(tuple_1[1: 4])
new_list.append(a)
print(new_list)

str_int = lambda x: int(x)
print(list(map(str_int, new_list)))






