"""Python program to interchange first and last element in the list"""

lst = input("Enter the list elements giving space between each item:").split(" ")
lst[0], lst[-1] = lst[-1], lst[0]
print(lst)
