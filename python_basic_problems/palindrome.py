# Python Program to Check Whether a String is Palindrome or Not

word = input("Enter the string:")
length = len(word)
b = -1
a = 0
if length % 2 == 0:
    for i in range(length // 2):
        if word[i] == word[b]:
            b -= 1
            a += 1
        else:
            print("Given string is not a palindrome")
            break

    if a >= 1:
        print("Given string is palindrome")
else:
    for i in range((length - 1) // 2):
        if word[i] == word[b]:
            b -= 1
            a += 1
        else:
            print("Given string is not a palindrome")
            break
    if a >= 1:
        print("Given string is palindrome")
