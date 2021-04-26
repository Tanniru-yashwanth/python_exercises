# the collatz sequence


def collatz(number):
    if number % 2 == 0:
        ans = number // 2
        print(ans)
        return ans
    else:
        ans_1 = (3 * number) + 1
        print(ans_1)
        return ans_1


num = int(input("Enter the integer: "))
while num != 1:
    num = collatz(num)

# collatz(3)
# collatz(10)
# collatz(5)
# collatz(16)
# collatz(8)
# collatz(4)
# collatz(2)
