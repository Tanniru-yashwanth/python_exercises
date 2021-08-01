"""12. a, b, c = 0, 0, 0 . Write a python program to print all permutations using those three variables

Output : 000 , 001 ,002, 003, 004, 0005 ,006, 007, 008, 009, 010, 011 …… 999"""

a, b, c = 0, 0, 0
for i in range(10):
    print(f"{a}{b}{c+i}")
