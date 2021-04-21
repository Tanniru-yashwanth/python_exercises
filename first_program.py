
def fizz_buzz(number):
    """
    Writing a fizz buzz program which does ...
    """
    if number % 3 == 0 and number % 5 == 0:
        return "FizzBuzz"
    elif number % 5 == 0:
        return "Buzz"
    elif number % 3 == 0:
        return "Fizz"
    else:
        return number


input_number = int(input("enter the number: "))
print(fizz_buzz(input_number))
