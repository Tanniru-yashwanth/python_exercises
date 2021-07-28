# Python Program to Extract Extension From the File Name

import os

file_name = "concepts.xlsx"
ext = os.path.splitext(file_name)
print(ext[1])
