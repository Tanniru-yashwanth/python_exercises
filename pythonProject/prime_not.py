# 10. Write a python program to check given number is prime or not

num = int(input("Enter the number:"))
lst = []
if num < 0:
    print("Given number is not positive")
elif num == 0 or num == 1:
    print("Given number is not prime")
else:
    for i in range(2, num):
        if num % i == 0:
            lst.append(i)
    if lst:
        print("Given number is not prime")
    else:
        print("Given number is prime")
