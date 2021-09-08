# 4. Write a python program to get the following output
# 1-----99
#
# 2-----98
#
# 3-----97
#
# . .
#
# . .
#
# . .
#
# 98-----2
#
# 99-----1

a = '-----'
for i in range(1, 100):
    print(f"{i}{a}{(100-i)}")
