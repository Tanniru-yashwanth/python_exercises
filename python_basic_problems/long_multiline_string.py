# Python Program to Create a Long Multiline String

string_input = list(input("Enter the  long string:"))
line = len(string_input) // 20
print(line)
final_list = []
for i in range(line):
    a = string_input[0:20]
    final_list.append(a)
    del string_input[0:20]
for x in final_list:
    print(''.join(x))
