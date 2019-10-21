"""
EXCEPTION

Program 3 module tries to catch various exceptions.

As is written, the main block raises three exceptions.
Rewrite three functions so that they handle specific exceptions.
Catch the exception and print the error message.
Each shall also have catch all exception handler with the generic error message.

If the program does not crash, then you have succeeded.

@author <Elijah Weske>
"""

import sys


def catch_file_not_found_error(filename):
    try:
        f = open(filename, 'r')
    except FileNotFoundError as e:
        print('Exception caught: File not found.')
    except Exception as e:
        print('Exception caught:', e)


def catch_division_by_zero_error(dividend, divisor):
    try:
        if divisor == 0:
            raise ValueError

        return dividend / divisor

    except ValueError:
        print('Exception Caught: Value Error - cannot divide by 0.')

    except Exception as e:
        print('Exception caught:', e)


def catch_index_error(list, index):
    try:
        if len(list) <= index:
            raise IOError('Index out of range.')

        return list[index]

    except IOError as e:
        print('Exception caught:', e)
    except Exception as e:
        print('Exception caught:', e)


if __name__ == '__main__':
    catch_file_not_found_error(sys.argv[0])
    catch_file_not_found_error('non_existing_file')     # exception error
    catch_division_by_zero_error(2, 3)
    catch_division_by_zero_error(2, 0)                  # exception error
    catch_index_error([1, 2, 3], 0)
    catch_index_error([1, 2, 3], 2)
    catch_index_error([1, 2, 3], 3)                     # exception error
