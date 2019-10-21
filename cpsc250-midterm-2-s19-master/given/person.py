"""
Simple class for a person
"""


class Person:

    def __init__(self, name, age):
        """
        Constructor for the Person class
        """
        self.name = name
        self.age = age

    def __str__(self):
        """
        Formatted string with instance information
        :return: string
        """
        return "{} ({})".format(self.name, self.age)
