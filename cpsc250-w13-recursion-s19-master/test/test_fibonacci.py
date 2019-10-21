import unittest
from inspect import signature

from src.fibonacci import *
import math

class TestFibonacci(unittest.TestCase):
    fib_seq = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597]

    def test_0_input_for_loop(self):
        fib = Fibonacci()
        self.assertEqual( 0, fib.fibonacci_loop(0),msg="fib[0]=0")

    def test_1_input_for_loop(self):
        fib = Fibonacci()
        self.assertEqual( 1, fib.fibonacci_loop(1),msg="fib[1]=1")

    def test_2_input_for_loop(self):
        fib = Fibonacci()
        self.assertEqual( 1, fib.fibonacci_loop(2),msg="fib[2]=1")

    def test_3_input_for_loop(self):
        fib = Fibonacci()
        self.assertEqual( 2, fib.fibonacci_loop(3),msg="fib[3]=2")
    def test_4_input_for_loop(self):
        fib = Fibonacci()
        self.assertEqual( 3, fib.fibonacci_loop(4),msg="fib[4]=3")
    def test_5_input_for_loop(self):
        fib = Fibonacci()
        self.assertEqual( 5, fib.fibonacci_loop(5),msg="fib[5]=5")
    def test_negative_for_loop(self):
        try:
            Fibonacci().fibonacci_loop(-1)
        except IndexError:
            try:
                Fibonacci().fibonacci_loop(-123)
            except IndexError:
                return # Successfully caught two IndexError

        self.fail(msg="Must raise a IndexError for negative indices")

    def test_loop_with_loop(self):
        for i in range(0,len(self.fib_seq)):
            exp = self.fib_seq[i]
            act = Fibonacci().fibonacci_loop(i)
            self.assertEqual(exp, act,msg="Fibonacci.fibonacci_loop failed expected {} not {} at index {}".format(exp,act,i))

    def test_0_input_for_recursion(self):
        fib = Fibonacci()
        self.assertEqual( 0, fib.fibonacci_recursion(0),msg="fib[0]=0")

    def test_1_input_for_recursion(self):
        fib = Fibonacci()
        self.assertEqual( 1, fib.fibonacci_recursion(1),msg="fib[1]=1")

    def test_2_input_for_recursion(self):
        fib = Fibonacci()
        self.assertEqual( 1, fib.fibonacci_recursion(2),msg="fib[2]=1")

    def test_3_input_for_recursion(self):
        fib = Fibonacci()
        self.assertEqual( 2, fib.fibonacci_recursion(3),msg="fib[3]=2")
    def test_4_input_for_recursion(self):
        fib = Fibonacci()
        self.assertEqual( 3, fib.fibonacci_recursion(4),msg="fib[4]=3")
    def test_5_input_for_recursion(self):
        fib = Fibonacci()
        self.assertEqual( 5, fib.fibonacci_recursion(5),msg="fib[5]=5")
    def test_negative_for_recursion(self):
        try:
            Fibonacci().fibonacci_recursion(-1)
        except IndexError:
            try:
                Fibonacci().fibonacci_recursion(-123)
            except IndexError:
                return # Successfully caught two IndexError

        self.fail(msg="Must raise a IndexError for negative indices")

    def test_recursion_with_loop(self):
        for i in range(0,len(self.fib_seq)):
            exp = self.fib_seq[i]
            act = Fibonacci().fibonacci_recursion(i)
            self.assertEqual(exp, act,msg="Fibonacci.fibonacci_recursion failed expected {} not {} at index {}".format(exp,act,i))




if __name__ == '__main__':
    unittest.main()
