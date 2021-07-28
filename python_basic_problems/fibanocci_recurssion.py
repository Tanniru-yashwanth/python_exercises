# Python Program to Display Fibonacci Sequence Using Recursion

def fib(number):
    if number <= 1:
        return number
    else:
        return fib(number - 1) + fib(number - 2)


number_in = int(input("Enter the number:"))
for x in range(number_in):
    print(fib(x))
