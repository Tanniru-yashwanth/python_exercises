# Python Program to Display Powers of 2 Using Anonymous Function

"""Program to display all the powers of 2 from zero to given number"""
number = int(input("Enter the number:"))
number_list = [x for x in range(number+1)]
power = lambda x: 2 ** x
number_list = list(map(power, number_list))
for i in number_list:
    print(i)

"""Program to display the power of 2 for only the given number"""
p = power(number)
print(f"The 2 power of the given number is :{p}")
