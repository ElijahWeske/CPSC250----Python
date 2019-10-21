import unittest

from src4.program4 import Program4
from inspect import signature

class TestProgram4(unittest.TestCase):

    def setUp(self):
        self.__delta = 0.000001    # used for allowable precision in computation.

    # ==========================================================================================================
    # Testing load_binary_data()
    # ==========================================================================================================
    # -------------------------------------------------------------------------------------------------
    # Test if the function is defined.
    # -------------------------------------------------------------------------------------------------
    def test_add_method_exists(self):
        # -----------------------------------------------------
        # Hey, if you can read unit tests here's a big hint
        # -----------------------------------------------------
        method = '__add__'

        self.assertTrue(hasattr(Program4, method),
                        msg='{} in module {} does not exist'.format(method, "program4"))

        class_method = getattr(Program4, method)
        actual = len(signature(class_method).parameters)

        expected = 2  # Just self
        self.assertEqual(expected, actual,
                         msg='{} should take {} parameter(s) but it takes {}.'.format(
                             method, "program4", expected, actual)
                         )

    def test_add_method_returns_instance(self):

        actual = Program4(3,4) + Program4(2,3)
        self.assertIsNotNone(actual,msg="Should return an instance of Program4")
        self.assertTrue(type(actual) is Program4,msg="Should return an instance of Program4")

    def test_add_method_works(self):
        actual = Program4(3, 4) + Program4(2, 3)
        self.assertIsNotNone(actual, msg="Should return an instance of Program4")
        self.assertTrue(type(actual) is Program4, msg="Should return an instance of Program4")
        self.assertEqual(5,actual.x,msg="Program4(3, 4) + Program4(2, 3) --> 3 + 2 = 5 for x-value")
        self.assertEqual(7,actual.y,msg="Program4(3, 4) + Program4(2, 3) --> 4 + 3 = 7 for y-value")

    def test_add_method_works2(self):
        actual = Program4(13, 4) + Program4(2, 13)
        self.assertIsNotNone(actual, msg="Should return an instance of Program4")
        self.assertTrue(type(actual) is Program4, msg="Should return an instance of Program4")
        self.assertEqual(15,actual.x,msg="Program4(13, 4) + Program4(2, 13) --> 13 + 2 = 15 for x-value")
        self.assertEqual(17,actual.y,msg="Program4(13, 4) + Program4(2, 13) --> 4 + 13 = 17 for y-value")

    def test_str_method_exists(self):
        # -----------------------------------------------------
        # Hey, if you can read unit tests here's a big hint
        # -----------------------------------------------------
        method = '__str__'

        self.assertTrue(hasattr(Program4, method),
                        msg='{} in module {} does not exist'.format(method, "program4"))

        class_method = getattr(Program4, method)
        actual = len(signature(class_method).parameters)

        expected = 1  # Just self
        self.assertEqual(expected, actual,
                         msg='{} should take {} parameter(s) but it takes {}.'.format(
                             method, "program4", expected, actual)
                         )

    def test_str_method_works2(self):
        actual = str(Program4(13, 4))
        self.assertIsNotNone(actual, msg="Converting to string should return an instance of string")
        self.assertTrue("(" in actual, msg="String should have a (")
        self.assertTrue(")" in actual, msg="String should have a )")
        self.assertTrue("13" in actual, msg="Program(13,4) should have a 13 in string")
        self.assertTrue("4"  in actual, msg="Program(13,4) should have a 4 in string")


    def test_str_method_works3(self):
        actual = str(Program4(9, -4))
        self.assertIsNotNone(actual, msg="Converting to string should return an instance of string")
        self.assertTrue("(" in actual, msg="String should have a (")
        self.assertTrue(")" in actual, msg="String should have a )")
        self.assertTrue("9" in actual, msg="Program(9, -4) should have a 9 in string")
        self.assertTrue("-4"  in actual, msg="Program(9, -4) should have a -4 in string")

    def test_str_method_works_exactly(self):
        actual = str(Program4(9, -4))
        self.assertIsNotNone(actual, msg="Converting to string should return an instance of string")
        self.assertEqual("(9, -4)", actual, msg="Program(9, -4) string should be (9, -4) exactly")


if __name__ == '__main__':
    unittest.main()
