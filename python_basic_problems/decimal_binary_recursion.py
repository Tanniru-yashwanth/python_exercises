# Python Program to Convert Decimal to Binary Using Recursion

def binary(number):
    if number > 1:
        binary(number // 2)
    print(number % 2, end='')


number = int(input("Enter the number:"))
binary(number)


