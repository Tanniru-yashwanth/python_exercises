# Python Program to Find LCM

number1 = int(input("Enter the first number:"))
number2 = int(input("Enter the second number:"))
lcm = []
for i in range(1, 100):
    if i % number1 == 0 and i % number2 == 0:
        lcm.append(i)
    else:
        pass
if lcm:
    print(lcm[0])
else:
    print("There is a lcm for the given numbers")
