"""6. Write a python program to read four numbers (representing the four octets of an IP) and
print the next five IP address

Eg:

Input:

192 168 255 252

----------Output---------

192 168 255 253

192 168 255 254

192 168 255 255

192 169 0 0

192 169 0 1"""


numbers = input("Enter the four numbers:").split(' ')
num_lst = reversed(list(map(int, numbers)))
for i in range(5):

