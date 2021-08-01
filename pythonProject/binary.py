"""5. Write a python program to read a number and
print the binary of that number (hint: if ‘a’ is a string ,
a[::-1] will be reverse of that string)"""


num = int(input("Enter the number:"))
quotient = num // 2
remainder = num % 2
lst_rem = [remainder]
while quotient != 0:
    num = quotient
    quotient = num // 2
    remainder = num % 2
    lst_rem.append(remainder)
lst = list(map(str, lst_rem))
print(''.join(reversed(lst)))