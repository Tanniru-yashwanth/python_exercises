# Python Program to Find Hash of File

import hashlib

file = open("S:/material/Python basic Programs..docx", 'rb')
hash_object = hashlib.md5()
for x in file:
    hash_object.update(x)
    m = hash_object.hexdigest()
print(m)
