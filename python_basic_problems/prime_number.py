# Python Program to Check Prime Number

number = int(input("Enter the number:"))
a = 0
for i in range(1, number+1):
    if number % i == 0:
        a += 1
    else:
        pass
if a == 2:
    print("Given number is prime")
else:
    print("Given number is not a prime")

