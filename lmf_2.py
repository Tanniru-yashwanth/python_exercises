"""Write a python program to add three given lists using python map and lambda"""

list_1 = [1, 2, 3, 4, 5]
list_2 = [6, 7, 8, 9, 10]
list_3 = [12, 13, 14, 15, 16]

add = lambda list1, list2, list3: list1 + list2 + list3
print(list(map(add, list_1, list_2, list_3)))
