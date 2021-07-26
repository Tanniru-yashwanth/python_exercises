# Python Program to Delete an Element From a Dictionary

dictionary = {1: 'q', 2: 'w', 3: 'e', 4: 'f'}
print(dictionary)
element = int(input("Enter the key of an element u want to delete :"))
dictionary.pop(element)
print(dictionary)
