x = 1
y = 1
z = 3
n = 3
list_1 = []
for i in range(0, x + 1):
    for j in range(0, y+1):
        for k in range(0, z+1):
            a = [i, j, k]
            if sum(a) != n:
                list_1.append(a)
print(list_1)

list_2 = [[b, c, d] for b in range(0, x+1) for c in range(0, y+1) for d in range(0, z+1) if b + c + d != n]
print(list_2)


