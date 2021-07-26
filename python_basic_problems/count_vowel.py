# Python Program to Count the Number of Each Vowel

a, i, e, o, u = 0, 0, 0, 0, 0
string_input = input("Enter the string:")
for x in string_input:
    if x == 'a':
        a += 1
    elif x == 'e':
        e += 1
    elif x == 'i':
        i += 1
    elif x == 'o':
        o += 1
    elif x == 'u':
        u += 1
print(f"a = {a}")
print(f"e = {e}")
print(f"i = {i}")
print(f"o = {o}")
print(f"u = {u}")
