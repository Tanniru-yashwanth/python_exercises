# Python Program to Find Factorial of Number Using Recursion

def fac(number):
    if number == 0:
        return 1
    return number * fac(number - 1)


in_number = int(input("Enter the number:"))
factorial = fac(in_number)
print(factorial)
