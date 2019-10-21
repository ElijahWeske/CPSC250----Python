import unittest
from inspect import signature

from src.my_very_own_error import MyVeryOwnError
from src.exceptions import Exceptions

class TestTime(unittest.TestCase):

    def test_my_very_own_error(self):
        err = MyVeryOwnError("test message")
        self.assertIsNotNone(err)
        self.assertTrue(isinstance(err,Exception))
        self.assertEqual("test message",str(err),msg="Error should have an error message associated with it.  Did you call Exception constructor?")

    def test_my_very_own_error2(self):

        method = '__init__'
        self.assertTrue(hasattr(MyVeryOwnError, method),
                        msg='The {} method in the MyVeryOwnError class in {} does not exist'.format(method, "my_very_own_error.py"))
        expected = 2
        class_method = getattr(MyVeryOwnError, method)
        actual = len(signature(class_method).parameters)
        self.assertEqual(expected, actual,
                         msg='MyVeryOwnError.{} should take {} parameter(s) but it takes {}. Does it have "self" and message data?'.format(
                             method, expected, actual)
                         )

    def test_exceptions_did_not_change_methods(self):

        method = 'throwSomething'
        self.assertTrue(hasattr(Exceptions, method),
                        msg='The {} method in the Exceptions class in {} does not exist'.format(method, "my_very_own_error.py"))
        expected = 1
        class_method = getattr(Exceptions, method)
        actual = len(signature(class_method).parameters)
        self.assertEqual(expected, actual,
                         msg='Exceptions.{} should take {} parameter(s) but it takes {}. As static it should not have a "self", just value?'.format(
                             method, expected, actual)
                         )

        method = 'catchSomething'
        self.assertTrue(hasattr(Exceptions, method),
                        msg='The {} method in the Exceptions class in {} does not exist'.format(method, "my_very_own_error.py"))
        expected = 1
        class_method = getattr(Exceptions, method)
        actual = len(signature(class_method).parameters)
        self.assertEqual(expected, actual,
                         msg='Exceptions.{} should take {} parameter(s) but it takes {}. As static it should not have a "self", just value?'.format(
                             method, expected, actual)
                         )


    def test_throw_something_negative(self):

        try:
            val = Exceptions.throwSomething(-1)
        except ValueError:
            try:
                val = Exceptions.throwSomething(-23495881) # try another one
            except ValueError:
                return # If we raised the error correctly, then return for successful test

        self.fail(msg="Negative value should throw a ValueError!")

    def test_throw_something_0(self):

        try:
            val = Exceptions.throwSomething(0)
        except OSError:
                return # If we raised the error correctly, then return for successful test

        self.fail(msg="0 should throw a OSError!")


    def test_throw_something_1(self):
        try:
            val = Exceptions.throwSomething(1)
        except FileNotFoundError:
            return  # If we raised the error correctly, then return for successful test

        self.fail(msg="1 should throw a OSError!")
    def test_throw_something_2(self):

        try:
            val = Exceptions.throwSomething(2)
        except MyVeryOwnError:
                return # If we raised the error correctly, then return for successful test

        self.fail(msg="2 should throw a MyVeryOwnError!")

    def test_throw_something_3(self):

        try:
            val = Exceptions.throwSomething(3)
            self.assertEqual(3,val,msg="not error should return value")
        except Exception as e:
            self.fail(msg="3 should NOT raise an Exception of any type! ({})".format(str(e)))

    def test_throw_something_453(self):

        try:
            val = Exceptions.throwSomething(453)
            self.assertEqual(453,val,msg="not error should return value")
        except Exception as e:
            self.fail(msg="453 should NOT raise an Exception of any type! ({})".format(str(e)))



    def test_catch_something_3(self):

        expected="3"
        try:
            val = Exceptions.catchSomething(int(expected))
            self.assertEqual(expected,val,msg="should return '{}' value not {}".format(expected, val))
        except Exception as e:
            self.fail(msg="catchSomething should NOT raise an Exception of any type! ({})".format(str(e)))


    def test_catch_something_345(self):

        expected="345"
        try:
            val = Exceptions.catchSomething(int(expected))
            self.assertEqual(expected,val,msg="should return '{}' value not {}".format(expected, val))
        except Exception as e:
            self.fail(msg="catchSomething should NOT raise an Exception of any type! ({})".format(str(e)))

    def test_catch_something_negative(self):

        expected="Negative values are not allowed"
        try:
            val = Exceptions.catchSomething(-3)
            self.assertEqual(expected,val,msg="should return '{}' value not {}".format(expected, val))
            val = Exceptions.catchSomething(-673)
            self.assertEqual(expected,val,msg="should return '{}' value not {}".format(expected, val))
        except Exception as e:
            self.fail(msg="catchSomething should NOT raise an Exception of any type! ({})".format(str(e)))

    def test_catch_something_0(self):

        expected="OS error"
        try:
            val = Exceptions.catchSomething(0)
            self.assertEqual(expected,val,msg="should return '{}' value not {}".format(expected, val))
        except Exception as e:
            self.fail(msg="catchSomething should NOT raise an Exception of any type! ({})".format(str(e)))

    def test_catch_something_1(self):

        expected=("File not found", 1)
        try:
            val = Exceptions.catchSomething(1)
            self.assertEqual(expected,val,msg="should return '{}' value not {}".format(expected, val))
        except Exception as e:
            self.fail(msg="catchSomething should NOT raise an Exception of any type! ({})".format(str(e)))


    def test_catch_something_2(self):

        expected= "My very own message"
        try:
            val = Exceptions.catchSomething(2)
            self.assertEqual(expected,val,msg="should return '{}' value not {}".format(expected, val))
        except Exception as e:
            self.fail(msg="catchSomething should NOT raise an Exception of any type! ({})".format(str(e)))


if __name__ == '__main__':
    unittest.main()
