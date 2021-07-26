# Python Program to Print the Fibonacci sequence

number = int(input("Enter the number:"))
a = 0
b = 1
if number == 0:
    print(0)
elif number == 1:
    print(1)
else:
    print(a)
    print(b)
    for i in range(number-2):
        c = a + b
        print(c)
        a = b
        b = c

