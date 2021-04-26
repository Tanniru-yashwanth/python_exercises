'''Write a function that accepts a list of items a person wants
on a sandwich. The function should have one parameter that collects as many
items as the function call provides, and it should print a summary of the sandwich that’s being ordered.
Call the function three times, using a different number of arguments each time'''


def sandwich(*items):
    print(f"sandwich ordered with {items}")


top_ups = ('veggies', 'sauces','cheese', 'butter')
sandwich(top_ups)
sandwich('chicken', 'sauces')
sandwich('panner', 'butter', 'cheese')
