import unittest

from src3 import program3
from inspect import signature
import os.path


class TestProgram3(unittest.TestCase):

    # ==========================================================================================================
    # Testing copy_file()
    # ==========================================================================================================
    # -------------------------------------------------------------------------------------------------
    # Test if the function is defined.
    # -------------------------------------------------------------------------------------------------
    def test_copy_file(self):
        # -----------------------------------------------------
        # Arrange
        # -----------------------------------------------------
        method = 'copy_file'

        # -----------------------------------------------------
        # Act and Assert
        # -----------------------------------------------------
        self.assertTrue(hasattr(program3, method),
                        msg='{} in module {} does not exist'.format(method, "program3"))

        class_method = getattr(program3, method)
        actual = len(signature(class_method).parameters)

        expected = 2
        self.assertEqual(expected, actual,
                         msg='{} should take {} parameter(s) but it takes {}.'.format(
                             method, "program3", expected, actual)
                         )

        actual = program3.copy_file(os.path.join("data", "text_data.txt"), os.path.join("data", "copy_text_data.txt"))
        self.assertIsNotNone(actual, msg='copy_file must return a number!')

    # -------------------------------------------------------------------------------------------------
    # Test if the function is defined.
    # -------------------------------------------------------------------------------------------------
    def test_copy_file2(self):
        source = os.path.join("data", "text_data.dat")
        target = os.path.join("data", "copy_text_data.txt")
        actual = program3.copy_file(source, target)
        self.assertEqual(0, actual, msg="The source file does not exist.")

    def test_copy_file3(self):
        source = os.path.join("data", "text_data.txt")
        target = os.path.join("data", "copy_text_data.txt")
        actual = program3.copy_file(source, target)
        self.assertEqual(3, actual, msg='The source file has 3 lines!')

        with open(source, 'r') as source_file:
            with open(target, 'r') as target_file:
                source_lines = source_file.readlines()
                target_lines = target_file.readlines()

        self.assertEqual(source_lines, target_lines, msg='source and target files are not the same!')


if __name__ == '__main__':
    unittest.main()
