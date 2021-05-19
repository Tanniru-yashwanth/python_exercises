"""Write a Python program to convert a given list of integers and a tuple of integers in a list of strings."""

list_integers = [23, 34, 76, 87, 90, 78]
tuple_integers = (45, 56, 78, 98, 90, 65)

string = lambda x: str(x)

print(list(map(string, list_integers)))
print(list(map(string, tuple_integers)))