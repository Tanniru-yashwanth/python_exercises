# Python Program to Return Multiple Values From a Function

def func_something(name):
    a = f"Hello Mr.{name} "
    b = f"Your username will be {name.title()}"
    c = f"Your email will be {name}@cygen.com"
    return a, b, c


print(func_something('yash'))
