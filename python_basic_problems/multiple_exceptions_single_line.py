# Python Program to Catch Multiple Exceptions in One Line


try:
    a = 2 / 0
    print(a)
except (TypeError, ZeroDivisionError) as e:
    print(f"{e}")
    print(f"you are entered the wrong data type or you are entered the zero for division")
