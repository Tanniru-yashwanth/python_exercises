"""Find all the numbers from 1-1000 that have a 6 in them"""

numbers = [i for i in range(1, 1000) if '6' in str(i)]
print(numbers)
