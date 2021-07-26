# Python Program to Check Armstrong Number

number = int(input("Enter the Number:"))
number1 = number
length = len(str(number))
arms = []
for i in range(length):
    a = number % 10
    arms.append(a)
    number = number // 10
func = lambda x: x ** length
arms1 = map(func, arms)
s = sum(arms1)
if s == number1:
    print("Given number is armstrong")
else:
    print("Given number is not a armstrong")
