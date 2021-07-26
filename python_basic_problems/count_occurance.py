# Python Program to Count the Occurrence of an Item in a List
from collections import Counter
list_input = list(input("Enter the list:").split(" "))

# for x in list_input:
#     a = 0
#     for y in list_input:
#         if x == y:
#             a += 1
#         else:
#             pass
#     print(f"occurrence of {x} is {a}")
#     for i in range(a):
#         list_input.remove(x)

count_dict = (Counter(list_input))
for x in count_dict.keys():
    print(f"Occurrence of {x} is {count_dict[x]}")
