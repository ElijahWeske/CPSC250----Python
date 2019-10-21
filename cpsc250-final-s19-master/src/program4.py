"""
ENCAPSULATION

Program 4 implements some of the encapsulation concept.

As written, class variables factor1 and factor2 are visbile
outside the class definition.

There are two levels of information hiding as a part of encapsulation:
    Level 1: by convention. the variable name is still accesible 
                but the naming convention is a kind of warning that
                it should not be accessed directly.
             Naturally, you will have to write getter and/or setter functions.

    Level 2: by name mangling. It is not accessible directly.
             Naturally, you will have to write getter and/or setter functions.

So, your task is to protect factor1 with Level 1 info hiding,
and protect factor2 and secret with Level 2 info hiding so that 
they are not accessible via variable names directly.

Once you modify the method, changing variable names and providing getter and setter methods,
modify the main so that it takes the advantage of the getter and setter functions.
@author <Elijah Weske>
"""


class SomeClass:
    _factor1 = 300
    __factor2 = 22

    def __init__(self, secret):
        self.__secret = secret

    def get_factor1(self):
        return SomeClass._factor1

    def set_factor1(self, new_fact):
        SomeClass._factor1 = new_fact

    def get_factor2(self):
        return SomeClass.__factor2

    def set_factor2(self, new_factor):
        SomeClass.__factor2 = new_factor

    def get_secret(self):
        return self.__secret

    def set_secret(self, secret):
        self.__secret = secret


if __name__ == '__main__':
    print(SomeClass._factor1)

    some = SomeClass('Alita')

    some.set_factor1(310)
    print(some.get_factor1())

    print(some.get_factor2())
    some.set_factor2(21)
    print(some.get_factor2())

    print(some.get_secret())
    some.set_secret('Shhh!')
    print(some.get_secret())

