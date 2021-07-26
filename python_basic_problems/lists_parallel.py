# Python Program to Iterate Through Two Lists in Parallel

list_one = input("Enter the first list elements giving space between each item:").split(" ")
list_two = input("Enter the first list elements giving space between each item:").split(" ")
for x in list_one:
    for y in list_two:
        print(y)
    print(x)
