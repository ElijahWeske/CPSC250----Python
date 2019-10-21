import unittest

from src5.program5 import Program5
from given.person import Person

from inspect import signature


class TestProgram5(unittest.TestCase):

    # ==========================================================================================================
    # Testing class Program5
    # ==========================================================================================================
    # -------------------------------------------------------------------------------------------------
    # Test if the function is defined.
    # -------------------------------------------------------------------------------------------------
    def test_init_method_exists(self):
        # -----------------------------------------------------
        # Hey, if you can read unit tests here's a big hint
        # -----------------------------------------------------
        method = '__init__'

        self.assertTrue(hasattr(Program5, method),
                        msg='{} in module {} does not exist'.format(method, "program5"))

        class_method = getattr(Program5, method)
        actual = len(signature(class_method).parameters)

        expected = 4
        self.assertEqual(expected, actual,
                         msg='{} should take {} parameter(s) but it takes {}.'.format(
                             method, "program5", expected, actual)
                         )

    def test_str_method_exists(self):
        # -----------------------------------------------------
        # Hey, if you can read unit tests here's a big hint
        # -----------------------------------------------------
        method = '__str__'

        self.assertTrue(hasattr(Program5, method),
                        msg='{} in module {} does not exist'.format(method, "program5"))

        class_method = getattr(Program5, method)
        actual = len(signature(class_method).parameters)

        expected = 1
        self.assertEqual(expected, actual,
                         msg='{} should take {} parameter(s) but it takes {}.'.format(
                             method, "program5", expected, actual)
                         )

    def test_inheritance(self):
        inst = Program5("Delci", 4, "super dog")
        self.assertIsInstance(inst, Person, msg="Program5 must inherit from Person class")

    def test_name(self):
        inst = Program5("Delci", 4, "super dog")
        self.assertEqual("Delci", inst.name, msg="Program5 must set name attribute")

    def test_age(self):
        inst = Program5("Delci", 4, "super dog")
        self.assertEqual(4, inst.age, msg="Program5 must set age attribute")

    def test_name_age(self):
        inst = Program5("Delci", 4, "super dog")
        self.assertEqual("Delci", inst.name, msg="Program5 must set name attribute")
        self.assertEqual(4, inst.age, msg="Program5 must set age attribute")

    def test_str_exact(self):
        inst = Program5("Chris", 458, "old hag")
        self.assertEqual("Chris (458) program5", str(inst), msg="Program5 string adds to Person string")

    def test_str_contains(self):
        inst = Program5("Chris", 458, "old hag")
        self.assertTrue("Chris" in str(inst), msg="Program5 string has name")
        self.assertTrue("458" in str(inst), msg="Program5 string has age")
        self.assertTrue("program5" in str(inst).lower(),
                        msg="Program5 string has program5")  # don't care about capitals


if __name__ == '__main__':
    unittest.main()
