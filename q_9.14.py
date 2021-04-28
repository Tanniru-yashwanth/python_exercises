'''Make a list or tuple containing a series of 10 numbers and
five letters. Randomly select four numbers or letters from the list and print a
message saying that any ticket matching these four numbers or letters wins a
prize'''


from random import choice


select = ['a', 'b', 'c', 'd', 'e', 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
a = choice(select)
b = choice(select)
c = choice(select)
d = choice(select)
print(f"Any ticket matching these numbers or letters {a}, {b}, {c}, {d} wins a prize")

