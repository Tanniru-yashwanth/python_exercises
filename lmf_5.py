"""Write a Python program to square the elements of a list using map() function"""

numbers = [2, 33, 45, 76, 89, 897]
square = lambda x: x * x
print(list(map(square, numbers)))
