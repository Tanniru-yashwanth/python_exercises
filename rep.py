import re

re_1 = re.compile(r'^hello$')
mo = re_1.search("hello")
print(mo.group())