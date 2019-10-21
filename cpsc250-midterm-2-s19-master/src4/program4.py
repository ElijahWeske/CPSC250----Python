"""
Program 4 Module defines 1 class that handles two numbers

__init__ is given.

You need to write __str__.

You need to write __add__ that handles operator overload "+".
    Program4(3, 4) + Program4(1, 2) should return an instance of Program4 with x = 4 and y = 6.

You may assume that I will only test with valid integers

@author Elijah Weske
"""


class Program4:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    # ^^^^ No need to modify above this line! ^^^^

    # Define a method to define string with parenthesis
    # Do NOT use f-strings!
    #  e.g. print(Program(3,4)) --> (3, 4)  - note the space after comma, but not by ( )
    def __str__(self):
        return f'({self.x}, {self.y})'

    # Define a method that will let you add to instances
    # You may assume that I will only try to add other instances of Program4
    #  print(Program4(3,4) + Program4(2,2)) --> (5,6)
    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return Program4(x, y)
