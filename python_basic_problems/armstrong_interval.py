# Python Program to Find Armstrong Number in an Interval

start_number = int(input("Enter the starting number:"))
end_number = int(input("Enter the end number:"))
for number in range(start_number, end_number + 1):
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
        print(f"{number1} is armstrong")
    else:
        pass
        # print(f"{number1} is not a armstrong")
