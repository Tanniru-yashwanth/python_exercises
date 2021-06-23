import re
import pyperclip

regex_phone_num = re.compile(r'''(
(\d{3}|\(\d{3}\))?      #areacode
(\s|-|\.)               #seperator
(\d{3}|\(\d{3}\))       #threedigit
(\s|-|\.)               #seperator
(\d{4}|\(\d{}4\))       #fourdigit
(\s*(ext|ext.)\s*(\d{2,5}))? #extension
)''', re.VERBOSE)


regex_email = re.compile(r'''
([a-zA-Z0-9._%+-]+         #name
@+                         #symbol
[a-zA-Z0-9.-]+             #domain 
(\.[a-zA-z]{2,4}))         #dot-something
''', re.VERBOSE)

text = str(pyperclip.paste())
matches = []
print(regex_phone_num.findall(text).group())
print(regex_email.group())
for groups in regex_phone_num.findall(text):
    phone_num = '-'.join(groups[1], groups[3], groups[5])
