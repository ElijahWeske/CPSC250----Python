"""
Simple class for a person
"""


class Hero:

    def __init__(self, super_power, catch_phrase=None):
        """
        Constructor for the Person class
        """
        self.super_power = super_power
        self.catch_phrase = catch_phrase

    def __str__(self):
        """
        Formatted string with instance information
        :return: string
        """
        if self.catch_phrase is None:
            return "{}".format(self.super_power)
        else:
            return "{} '{}'".format(self.super_power, self.catch_phrase)
