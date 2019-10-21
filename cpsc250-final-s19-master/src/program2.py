"""
INHERITANCE

Program 2 module defines a parent class and a child class.

The parent class name is Automobile with the following attributes:
    make
    year

    The contstructor __init__ shall accept these two parameters, position dependent.
    The string representation of this class __str__ shall return:
        Make: <make>
        Year: <year>

The child class name is Model with the following attributes:
    model_name
    transmission
    number_of_doors

    The constructor __init__ shall accept these three parameters in addition to
    the two parameters for the parent class.
    The string representation of this class __str__ shall return:
        Make: <make>
        Year: <year>
        Model: <model_name>
        Transmission: <transmission>
        Doors: <number_of_doors>

@author <Elijah Weske>
"""

class Automobile():
    def __init__(self, make, year):
        self.make = make
        self.year = year

    def __str__(self):
        return f'Make: {self.make} \nYear: {self.year}'


class Model(Automobile):
    def __init__(self, make, year, model_name, transmission, number_of_doors):
        Automobile.__init__(self, make, year)
        self.model_name = model_name
        self.transmission = transmission
        self.number_of_doors = number_of_doors

    def __str__(self):
        return f'{Automobile.__str__(self)} \nModel: {self.model_name} \nTransmission: {self.transmission} ' \
               f'\nDoors: {self.number_of_doors}'


if __name__ == '__main__':
    print(Automobile('Dodge', 2018))
    # should print:
    # Make: Dodge
    # Year: 2018

    print(Model('Dodge', 2018, 'Ram', 'Automatic', 4))
    # should print:
    # Make: Dodge
    # Year: 2018
    # Model: Ram
    # Transmission: Automatic
    # Doors: 4
