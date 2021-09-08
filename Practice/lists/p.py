"""Write a function called unique_english_letters that takes the string word as a parameter.
The function should return the total number of unique letters in the string. Uppercase and
lowercase letters should be counted as different letters.

We’ve given you a list of every uppercase and lower case letter in the English alphabet.
It will be helpful to include that list in your function"""

from collections import Counter


def unique_english_letters(word):
    a = Counter(word)
    return len(a.keys())


print(unique_english_letters("apple"))
