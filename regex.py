import re
reg = re.compile('batman')
mo = reg.findall('The fav is batman and i love batman ')
a = 0
for x in mo:
    a += 1
print(a)
