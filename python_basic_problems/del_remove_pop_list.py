# Python Program to Differentiate Between del, remove, and pop on a List

list_input = [1, 2, 5, 6, 'i', 'th']
print(list_input)


"""pop needs a index and will return the item u removed"""
print(list_input.pop())
print(list_input)


"""remove will return none"""
print(list_input.remove(5))
print(list_input)


"""del will required the index of element u needed"""
del list_input[2]
print(list_input)
