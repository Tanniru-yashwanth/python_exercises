"""Write a Python program to compute the square of first N Fibonacci numbers,
 using map function and generate a list of the numbers"""


def fib(num):
    n1 = 0
    n2 = 1
    series = 0
    for i in range(num):
        print(series, end=' ')
        n1 = n2
        n2 = series
        series = n1 + n2


n = [1, 100]
fib_1 = list(map(fib, n))


def squares(x):
    a = x * x
    return a


squares_list = list(map(squares, fib_1))
print(squares_list)


