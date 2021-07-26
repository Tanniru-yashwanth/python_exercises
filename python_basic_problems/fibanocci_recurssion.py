# Python Program to Display Fibonacci Sequence Using Recursion

def fib(number):
    if number == 0:
        print(0)
    elif number == 1:
        print(1)
    else:
        a = 0
        b = 1
        print(a)
        print(b)
        for i in range(number):
            c = a + b
            print(c)
            a = b
            b = c


def fiba():
    number = int(input("Enter the number:"))
    fib(number)


fiba()
