# Python Program to Print all Prime Numbers in an Interval(200,500)


for x in range(200, 501):
    a = 0
    for y in range(1, x+1):
        if x % y == 0:
            a += 1
        else:
            pass
    if a == 2:
        print(x)
