# Python Program to Find ASCII Value of Character

character = input("Enter the character:")
dict_character = dict()
list_alphabets_upper = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S',
                        'T',
                        'U', 'V', 'W', 'X', 'Y', 'Z']
list_alphabets_lower = [x.lower() for x in list_alphabets_upper]
list_alphabets_upper_number = [x for x in range(65, 91)]
list_alphabets_lower_number = [y for y in range(97, 123)]
list_alphabets = list_alphabets_upper + list_alphabets_lower
list_numbers = list_alphabets_upper_number + list_alphabets_lower_number
dict_character = {k: v for k, v in zip(list_alphabets, list_numbers)}
print(dict_character[character])
