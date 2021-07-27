# Python Program to Measure the Elapsed Time in Python
import time

time_start = time.time()
# print(time_start)
number = int(input("Enter the decimal:"))
number1 = number


def binary(number):
    print(f"Binary for {number}")
    list_bin = []
    quotient = number // 2
    remainder = number % 2
    list_bin.append(remainder)
    while quotient != 0:
        number = quotient
        quotient = number // 2
        remainder = number % 2
        list_bin.append(remainder)
    f_list = list(reversed(list_bin))
    # print(f"Binary code for the {number1} ")
    for x in f_list:
        print(x, end='')
    print('\n')


def octal(number):
    print(f"Octal for {number}")
    list_oct = []
    quotient = number // 8
    remainder = number % 8
    list_oct.append(remainder)
    while quotient != 0:
        number = quotient
        quotient = number // 8
        remainder = number % 8
        list_oct.append(remainder)
    f_list = list(reversed(list_oct))
    # print(f"Octal for {number1} ")
    for x in f_list:
        print(x, end='')
    print('\n')


def hexa(number):
    print(f"Hexadecimal for {number}")
    list_hexa = []
    quotient = number // 16
    remainder = number % 16
    list_hexa.append(remainder)
    while quotient != 0:
        number = quotient
        quotient = number // 16
        remainder = number % 16
        list_hexa.append(remainder)
    f_list = list(reversed(list_hexa))
    # print(f"Octal for {number1} ")
    for x in f_list:
        print(x, end='')
    print('\n')


binary(number)
octal(number)
hexa(number)

time_end = time.time()
# print(time_end)
time_taken = time_end - time_start
# print(time.process_time())
print(f" The time taken to complete the task is {time_taken}")
