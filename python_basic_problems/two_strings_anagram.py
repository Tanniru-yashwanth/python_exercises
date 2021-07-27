# Python Program to Check If Two Strings are Anagram

string_one = list(input("Enter the first string:"))
string_two = list(input("Enter the second string:"))
set_one = set(string_one)
length = len(set_one)
set_two = set(string_two)
list_same = []
for x in set_one:
    for y in set_two:
        if x == y:
            list_same.append(x)
        else:
            pass
if len(list_same) == length:
    print("Given two strings are anagram")
else:
    print("Given two strings are not anagram")
