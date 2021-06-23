"""if __name__ == '__main__':
    s = 'qA2'
    alphanumeric = []
    alphabetical = []
    digits = []
    lower_chars = []
    upper_chars = []
    for x in s:
        if not x.isalnum():
            alphanumeric.append(False)
        else:
            alphanumeric.append(True)

        if not x.isalpha():
            alphabetical.append(False)
        else:
            alphabetical.append(True)

        if not x.isdigit():
            digits.append(False)
        else:
            digits.append(True)

        if not x.islower():
            lower_chars.append(False)
        else:
            lower_chars.append(True)

        if not x.isupper():
            upper_chars.append(False)
        else:
            upper_chars.append(True)

    print(True) if True in alphanumeric else print(False)
    print(True) if True in alphabetical else print(False)
    print(True) if True in digits else print(False)
    print(True) if True in lower_chars else print(False)
    print(True) if True in upper_chars else print(False)
"""


"""def solve(s):
    l = s.split(" ")
    l_1 = []
    for x in l:
        if len(x) > 1:
            if x[0].isdigit():
                l_1.append(x)
            else:
                l_1.append(x.title())
        else:
            l_1.append(x.title())
    return " ".join(l_1)


S = "hello world"
print(solve(S))"""
"""a = 3
b = 1
try:
    print(int(a) // int(b))
except ZeroDivisionError as e:
    print(f"Error code: {e}")
except ValueError as v:
    print(f"Error code: {v}")"""


s = {1, 2, 3, 4, 5, 6, 7, 8, 9}
i = "remove 9"
if i == 'pop':
    s.pop()
else:
    c = i.split(" ")
    if c[0] == "remove":
        s.remove(c[1])
    if c[0] == "discard":
        s.discard(c[1])
print(s)
"""from collections import Counter

rl = "4291 240 4231 99 2727 1566 110 3166 4046 752 4236 414 926 1521 3322 1112 497 888 1280 3631 524 3999 461 4552 " \
     "1742 2790 3220 1608 547 2897 1006 3551 2881 1753 1785 796 2793 4103 1668 520 1454 767 1406 1699 2155 3401 2920 " \
     "3169 298 1969 774 2566 546 3417 2035 1376 3007 870 3767 241 767 674 1259 3838 77 991 2639 2699 1500 4478 2706" \
     " 3664 3576 1079 842 1359 1034 372 3824 1662 1177 2072 4269 3203 2252 192 1923 2471 266 4161 2899 2629 1029 2077 " \
     "1253 275 1552 1835 3863 2628 108 85 1420 4183 2457 2611 4503 3388 1727 3840 2668 3596 373 807 316 203 117 3455" \
     " 2739 578 3827 1639 71 4377 629 956 487 2651 1127 1254 1700 1365 3964 3234 2546 562 1003 308 1531 4466 4141 1189 " \
     "752 1807 1837 1878 2944 3422 1399 1605 3347 2649 198 1730 4276 3834 4577 3533 3567 3951 1968 2345 2809 1503 " \
     "2299 3067 2298 2053 4321 1255 684 4444 3658 4411 3232 422 247 4169 535 4368 13 2183 2635 621 4046 2174 2430 " \
     "2938 4444 181 4131 1403 1479 2149 1931 46 4237 347 3759 228 2820 332 3083 3387 356 3421 4343 2198 923 1294 " \
     "2483 " \
     "2799 959 677 2994 4585 2870 13"
k = 5
li = rl.split()
print(Counter(li))"""

