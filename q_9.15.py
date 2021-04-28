'''You can use a loop to see how hard it might be to win
the kind of lottery you just modeled. Make a list or tuple called my_ticket.
Write a loop that keeps pulling numbers until your ticket wins. Print a message
reporting how many times the loop had to run to give you a winning ticket.'''


from random import choice

my_ticket = ['a', 'b', 'c', 'd', 'e', 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
temp = 0
while True:
    a = choice(my_ticket)
    temp += 1
    if a == 'e':
        break
print(f"The loop has to run {temp} times to give you a winning ticket")
