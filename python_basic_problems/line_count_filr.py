# Python Program to Get Line Count of a File

file = open("S:/material/completed.txt", 'r')
file_object = file.readlines()
line_count = len(file_object)
print(f"The number of lines in file is {line_count}")
a = 1
for x in file_object:
    b = len(x)
    print(f"The count of characters in {a} line is {b}")
    a += 1

