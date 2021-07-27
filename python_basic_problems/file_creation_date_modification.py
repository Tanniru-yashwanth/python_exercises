# Python Program to Get File Creation and Modification Date


import os
import time
import datetime
path = r"S:/material/completed.txt"
creation_time = os.path.getctime(path)
creation_time_sec = time.ctime(creation_time)
print(f"The file was created on  - {creation_time_sec}")
modification_date = os.path.getmtime(path)
modification_date_ = time.ctime(modification_date)
print(f"The file was last modified on  - {modification_date_}")