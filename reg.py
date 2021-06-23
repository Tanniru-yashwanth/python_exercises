import re
"""reg_object = re.compile(r'([QWRTYPSDFGHJKLZXCVBNMqwrtypsdfghjklzxcvbnm])([aeiouAEIOU]{2,})([QWRTYPSDFGHJKLZXCVBNMqwrtypsdfghjklzxcvbnm])')
l = reg_object.findall('abaabaabaabaae')
print(l)
for x in l:
    print(x[1])"""

"""for i in range(0, 6):
    m = re.search(r'aa', 'aaadaa')
    print(m.group())"""

"""pattern = r"([a-zA-Z0-9])\1+"
string = "..12345678910111213141516171820212223"
mo = re.search(pattern, string)
print(mo.group(1))"""


# S = "abaabaabaabaae"
# pattern = r'([QWRTYPSDFGHJKLZXCVBNMqwrtypsdfghjklzxcvbnm])([aeiouAEIOU]{2,})([qwrtypsdfghjklzxcvbnmQWRTYPSDFGHJKLZXCVBNM])'
# print(list(re.finditer(pattern, S)))
# l = list(map(lambda x: x.group(2), re.finditer(pattern, S)))
# print(l)
# if l:
#     for x in l:
#         print(x)
# else:
#     print(-1)


"""def fun(s):
    # return True if s is a valid email, else return False
    if re.match(r'(\.)([a-zA-Z]){3}', s):
        return True
    else:
        return False


x = ["3", "learn.point@learningpoint.net", "learnpoint@learningpoint.net", "learnpoint@learningpoint.net1", "mike13445@yahoomail9.server"]
print(list(filter(fun, x)))"""

#for i in range(T):
a = "0"
if re.match(r'(^(\+|\-|\.|(\-\.)|(\+\.))?\d+(\.\d+)?$)', a):
    print(True)
else:
    print(False)

"""string = "x  & &&| && ||  ||  |x"""
"""if re.search(r'\s&&\s', string):
        print(re.sub(r'\s&&\s', ' and ', string))"""
"""elif re.search(r'\s\|\|\s', string):
        print(re.sub(r'\s\|\|\s', ' or ', string))
else:
        print(string)"""
"""string = '85234789651'
if re.match(r'^(7|8|9)(\d{9})$', string):
    print("YES")
else:
    print("NO")"""

"""n, m = "VIRUS <virus!@variable.:p>".split()
print(n, m)
if re.match(r'[a-zA-Z0-9.-_]+@[a-zA-Z]+\.[a-zA-Z]{3}', m):
    print(n, m)"""

# S = "aaadaa"
# k = "aa"
# r = re.compile(r'(?=(q))')
# m = r.finditer("hbcasckjabchsdcsdcgvdsjhvcb")
#
# for match in m:
#     print(match.group(1))
#     print(match.start(1))
#     print(match.end(1) - 1)
# S = "aaadaa"
# k = "aa"
# m = re.finditer(f'(?=({k}))', S)
# matches = [match for match in m]
# if matches:
#     for match in matches:
#         print(match.start(1), (match.end(1) - 1))
# else:
#     print((-1, -1))

# if re.search(r'^(\+|\-|\.|\-.|\+.)?\d+(\.\d+)?$', '+-1.5486468'):
#     print(True)
# else:
#     print(False)