# 7. Write a python program to print the factorial of a given number

num = int(input("Enter the number:"))
result = 1
for i in range(1, num+1):
    result = result * i
print(result)