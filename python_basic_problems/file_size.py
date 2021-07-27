# Python Program to Check the File Size

import os
path = 'S:/material/concepts.xlsx'
size = os.path.getsize(path)
print(f"The size of file is {size} bytes")
