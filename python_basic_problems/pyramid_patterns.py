# Python Program to Create Pyramid Patterns

"""Program to print half pyramid"""


def pyramid():
    number = int(input("Enter the size number of pyramid:"))
    a = '*'

    for i in range(number + 1):
        print(i * a)


"""Program to print inverted half pyramid"""


def inverted_pyramid():
    number = int(input("Enter the size number of pyramid:"))
    a = '*'

    for i in range(number + 1):
        print(number * a)
        number -= 1


pyramid()
inverted_pyramid()
