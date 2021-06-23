"""n = int(input("enter the no of inputs:"))
i = 0
a = set()
for i in range(0, n):
    country = input("enter the countries:")
    a.add(country)
print(len(a))

"""
"""i = 2
print(i, end='i')"""
"""s = "123"
for x in s:
    if not x.isalpha():
        print(False)
        continue
    else:
        print(True)"""


"""def fibonacci(n):
    n1 = 0
    n2 = 1
    list_1 = []
    for i in range(0, n):
        list_1.append(n1)
        n3 = n1 + n2

        n1 = n2
        n2 = n3
    return list_1


print(fibonacci(1))"""

c = "H"
thickness = 5
for i in range(thickness):
    print((c*i).rjust(thickness-1, '-')+c+(c*i).ljust(thickness-1, '-'))

