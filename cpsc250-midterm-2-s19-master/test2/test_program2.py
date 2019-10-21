import unittest

from src2 import program2
from inspect import signature
import os.path


class TestProgram2(unittest.TestCase):

    # ==========================================================================================================
    # Testing search_text_data()
    # ==========================================================================================================
    # -------------------------------------------------------------------------------------------------
    # Test if the function is defined.
    # -------------------------------------------------------------------------------------------------
    def test_search_text_data(self):
        # -----------------------------------------------------
        # Arrange
        # -----------------------------------------------------
        method = 'search_text_data'

        # -----------------------------------------------------
        # Act and Assert
        # -----------------------------------------------------
        self.assertTrue(hasattr(program2, method),
                        msg='{} in module {} does not exist'.format(method, "program2"))

        class_method = getattr(program2, method)
        actual = len(signature(class_method).parameters)

        expected = 2
        self.assertEqual(expected, actual,
                         msg='{} should take {} parameter(s) but it takes {}.'.format(
                             method, "program2", expected, actual)
                         )

        actual = program2.search_text_data(os.path.join("data", "text_data.txt"), '')
        self.assertIsNotNone(actual, msg='search_text_data must return a number!')

    # -------------------------------------------------------------------------------------------------
    # Test if the function is defined.
    # -------------------------------------------------------------------------------------------------
    def test_search_text_data2(self):
        actual = program2.search_text_data(os.path.join("data", "text_data.txt"), 'of')
        self.assertEqual(2, actual, msg="The text input data has only 2 occurrences of the word 'of'.")

    def test_search_text_data3(self):
        actual = program2.search_text_data(os.path.join("data", "text_data.txt"), 'None')
        self.assertEqual(0, actual, msg="The text input data has no occurrence of the word 'None'.")

    def test_search_text_data4(self):
        actual = program2.search_text_data(os.path.join("data", "text_data.dat"), 'None')
        self.assertEqual(-1, actual, msg="If the input file does not exist, it must return -1.")


if __name__ == '__main__':
    unittest.main()
