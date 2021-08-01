# 3. Write a python program to read three numbers (a,b,c) and
# check how many numbers between ‘a’ and ‘b’ are divisible by ‘c’

a = int(input("Enter the first number:"))
b = int(input("Enter the second number:"))
c = int(input("Enter the third number:"))
num = 0
for i in range(a + 1, b):
    if i % c == 0:
        num += 1
print(num)