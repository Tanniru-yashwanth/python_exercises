# Python Program to Trim Whitespace From a String

"""Using for loop"""
string_input = input("Enter the string:").split()
for x in string_input:
    if x == " ":
        string_input.remove(x)
print(''.join(string_input))

"""Without using for loop"""
string_input = input("Enter the string:").split(" ")
print(''.join(string_input))

"""Without using split method"""
string_input = input("Enter the string:")
l = []
for x in string_input:
    if x != " ":
        l.append(x)
print(''.join(l))
