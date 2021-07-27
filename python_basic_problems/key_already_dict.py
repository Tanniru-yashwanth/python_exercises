# Python Program to Check if a Key is Already Present in a Dictionary

dictionary = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
key = input("Enter the key u want to check:")
a = 0
for x in dictionary.keys():
    if x == key:
        a += 1
        print("Key is present in dictionary")
if a == 0:
    print("Key is not present in dictionary")
