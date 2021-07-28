# # Python Program to Represent enum

from enum import Enum


class Something(Enum):
    dog = 'max'
    cat = 'mini'


print(Something.dog)
