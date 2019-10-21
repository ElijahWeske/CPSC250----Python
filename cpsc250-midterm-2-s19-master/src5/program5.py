"""
Program 5 defines 1 class called Program5

Inherit from Person class.
Use the same name, age arguments in constructor, and
make use of Person constructor for full credit

Override the Person's str conversion method to
add a space and "program5" to the end the string  (do NOT modify Person)

@author <your name here>
"""

from given.person import Person  # You might need this
from given.hero import Hero  # You might need this


class Program5(Person, Hero):
    def __init__(self, name, age, power=None):
        super().__init__(name, age)
        self.power = power

    def __str__(self):
        return f'{super().__str__()} program5'