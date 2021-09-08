num_tests = int(input())
for i in range(num_tests):
    l = input().split(' ')
    lst = input().split(" ")
    for x in range(int(l[1])):
        lst.insert(0, lst[-1])
        lst.pop()
    print(' '.join(lst))