import unittest
from inspect import signature

from src.factorial import *
import math

class TestFactorial(unittest.TestCase):

    def test_0_input_for_loop(self):
        self.assertEqual( 1, factorial_loop(0),msg="0!=1")

    def test_1_input_for_loop(self):
        self.assertEqual(1, factorial_loop(1), msg="1!=1")

    def test_2_input_for_loop(self):
        self.assertEqual(2, factorial_loop(2), msg="2!=2")

    def test_negative_for_loop(self):
        try:
            factorial_loop(-1)
        except ValueError:
            try:
                factorial_loop(-123)
            except ValueError:
                return # Successfully caught two ValueErrors

        self.fail(msg="Must raise a ValueError for negative inputs")

    def test_loop_with_loop(self):
        for i in range(2,15):
            exp = math.factorial(i)
            act = factorial_loop(i)
            self.assertEqual(exp, act,msg="factorial_loop failed expected {} not {}".format(exp,act))


    def test_0_input_for_recursion(self):
        self.assertEqual( 1, factorial_recursion(0),msg="0!=1")

    def test_1_input_for_recursion(self):
        self.assertEqual(1, factorial_recursion(1), msg="1!=1")

    def test_2_input_for_recursion(self):
        self.assertEqual(2, factorial_recursion(2), msg="2!=2")

    def test_negative_for_recursion(self):
        try:
            factorial_recursion(-1)
        except ValueError:
            try:
                factorial_recursion(-123)
            except ValueError:
                return # Successfully caught two ValueErrors

        self.fail(msg="Must raise a ValueError for negative inputs")

    def test_recursion_with_loop(self):
        for i in range(2,15):
            exp = math.factorial(i)
            act = factorial_recursion(i)
            self.assertEqual(exp, act,msg="factorial_recursion failed expected {} not {}".format(exp,act))


if __name__ == '__main__':
    unittest.main()
