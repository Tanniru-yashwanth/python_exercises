"""11. Write a python program to print all prime numbers between 0 to 100 ,
and print how many prime numbers are there."""

lst_prime = []
for num in range(0, 100):
    lst = []
    for i in range(1, num):
        if num % i == 0:
            lst.append(i)
    if len(lst) == 1:
        print(num)
        lst_prime.append(num)
a = len(lst_prime)
print(f"total number of prime numbers:{a}")




