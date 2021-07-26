# Python Program to Get a Substring of a String

import re
string_input = input("Enter the string:")
substring_input = input("Enter the substring:")
re_object = re.compile(substring_input)
search = re_object.findall(string_input)
for x in search:
    print(x)
