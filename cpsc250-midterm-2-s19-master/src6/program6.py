"""
Program 6 defines 1 class called Program6

Inherit from both Person and Hero classes.
Use the same name, age, super_power, and catch_phrase arguments in constructor, and
make use of both Person and Hero constructors for full credit

Override the str conversion method to combine Person and Hero strings

@author <your name here>
"""

from given.person import Person
from given.hero import Hero


class Program6(Person, Hero):
    def __init__(self, name, age, super_power, catch_phrase):
        pass


    def __str__(self):
        pass
