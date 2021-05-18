"""For all the numbers 1-1000, use a nested list/dictionary comprehension to
find the highest single digit any of the numbers is divisible by."""

Number = [max([x for x in range(1, 10) if y % x == 0]) for y in range(1, 1000)]
print(Number)
