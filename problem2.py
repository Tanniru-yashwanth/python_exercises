# add try and except clause

def collatz(number):
    if number % 2 == 0:
        ans = number // 2
        print(ans)
        return ans
    else:
        ans_1 = (3 * number) + 1
        print(ans_1)
        return ans_1


try:
    num = int(input("Enter the integer: "))
except ValueError:
    print('must enter a integer')
while num != 1:
    num = collatz(num)
