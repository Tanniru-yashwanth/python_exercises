# Python Program to Find HCF or GCD

number1 = int(input("Enter the first number:"))
number2 = int(input("Enter the second number:"))
list_number1 = []
list_number2 = []
for i in range(1, number1+1):
    if number1 % i == 0:
        list_number1.append(i)
    else:
        pass
for i in range(1, number2):
    if number2 % i == 0:
        list_number2.append(i)
    else:
        pass
list_common = []
for x in list_number1:
    for y in list_number2:
        if x == y:
            list_common.append(x)
        else:
            pass
print(list_common[-1])
