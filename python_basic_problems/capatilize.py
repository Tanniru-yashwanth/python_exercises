# Python Program to Capitalize the First Character of a String

string_input = input("Enter the string:").split(" ")
a = string_input[0].capitalize()
string_input.remove(string_input[0])
string_input.insert(0, a)
print(''.join(string_input))
