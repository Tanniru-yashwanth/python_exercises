# Python Program to Differentiate Between type() and isinstance()

input_enter = input("Enter the input:")
a = type(input_enter)
"""Type function describes the type of the input i.e, it shows the class"""
print(a)
"""isinstance function checks whether the input is the instance of the class"""
print(isinstance(input_enter, a))
