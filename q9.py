'''9.write  code that prints hello if 1 is stored in spam,prints Howdy if 2 is stored in spam,and prints Greetings!
if anything else is stored in spam.'''


spam = int(input("enter the number: "))

if spam == 1:
    print('Hello')
elif spam == 2:
    print('Howdy')
else:
    print('Greetings!')

