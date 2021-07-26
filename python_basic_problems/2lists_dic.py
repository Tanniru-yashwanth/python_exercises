# Python Program to Convert Two Lists Into a Dictionary

list_one = input("Enter the first list elements:").split(" ")
list_two = input("Enter the second list elements:").split(" ")
dictionary = {}
for i in range(len(list_one)):
    dictionary[list_one[i]] = list_two[i]
print(dictionary)
