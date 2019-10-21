"""
Program 1 Module defines 1 recursive function.

factorial_on_even_numbers returns factorial of even numbers.

Typically, a factorial of n is 1 * 2 * ... * n.
But this function computes factorial only for even numbers.
For example, if number is 7, this returns
    1 * 2 * 4 * 6

Even though you can write this with for loop efficiently,
you shall write it in a recursive function for the learning purpose.

:param number:
:return: factorial on even numbers only

@author <Elijah Weske>
"""


def factorial_on_even_numbers(number):
    if number <= 1:
        return 1

    if number % 2 != 0:
        number -= 1

    return number * factorial_on_even_numbers(number - 2)


if __name__ == '__main__':
    print(factorial_on_even_numbers(0))     # 1
    print(factorial_on_even_numbers(1))     # 1
    print(factorial_on_even_numbers(2))     # 2
    print(factorial_on_even_numbers(5))     # 8
    print(factorial_on_even_numbers(7))     # 48
    print(factorial_on_even_numbers(8))     # 384
