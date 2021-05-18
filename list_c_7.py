"""Use a nested list comprehension to find all the numbers from 1-1000
that are divisible by any single digit besides 1(2-9)"""

Numbers = [x for x in range(1, 1000)if True in [True for y in range(2, 10) if x % y == 0]]
print(Numbers)
