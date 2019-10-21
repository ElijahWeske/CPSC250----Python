import unittest

from src1 import program1
from inspect import signature
import os.path

import given.create_data as create_data


class TestProgram1(unittest.TestCase):

    # ==========================================================================================================
    # Testing load_csv()
    # ==========================================================================================================
    # -------------------------------------------------------------------------------------------------
    # Test if the function is defined.
    # -------------------------------------------------------------------------------------------------
    def test_load_csv(self):
        # -----------------------------------------------------
        # Arrange
        # -----------------------------------------------------
        method = 'load_csv'

        # -----------------------------------------------------
        # Act and Assert
        # -----------------------------------------------------
        self.assertTrue(hasattr(program1, method),
                        msg='{} in module {} does not exist'.format(method, "program1"))

        class_method = getattr(program1, method)
        actual = len(signature(class_method).parameters)

        expected = 1
        self.assertEqual(expected, actual,
                         msg='{} should take {} parameter(s) but it takes {}.'.format(
                             method, "program1", expected, actual)
                         )

        actual = program1.load_csv(os.path.join("data", "short_test_data.csv"))
        self.assertIsNotNone(actual, msg='load_csv must return data!')

    # -------------------------------------------------------------------------------------------------
    # Test if the function is defined.
    # -------------------------------------------------------------------------------------------------
    def test_load_csv2(self):

        actual = program1.load_csv(os.path.join("data", "short_test_data.csv"))
        self.assertIsNotNone(actual, msg='load_csv must return data!')
        self.assertTrue(len(actual) > 2, msg='load_csv must return multiple data elements!')

    def test_load_csv3(self):

        actual = program1.load_csv(os.path.join("data", "short_test_data.csv"))
        self.assertIsNotNone(actual, msg='load_csv must return data!')
        self.assertEqual(len(actual), 3, msg='load_csv must return 3 data elements!')

    def test_load_csv4(self):

        c1, c2, c3 = program1.load_csv(os.path.join("data", "short_test_data.csv"))
        self.assertEqual(len(c1), 8, msg='short data file has 8 elements in first column!')
        self.assertEqual(len(c2), 8, msg='short data file has 8 elements in second column!')
        self.assertEqual(len(c3), 8, msg='short data file has 8 elements in third column!')

    def test_load_csv5(self):

        c1e, c2e, c3e = create_data.make_csv_data(8)
        c1a, c2a, c3a = program1.load_csv(os.path.join("data", "short_test_data.csv"))
        self.assertEqual(c1e, c1a, msg='short data file has 8 elements in first column!')
        for i in range(len(c2e)):
            self.assertAlmostEqual(c2e[i], c2a[i], msg='short data file has 8 elements in second column!')
        for i in range(len(c3e)):
            self.assertAlmostEqual(c3e[i], c3a[i], msg='short data file has 8 elements in third column!')

        # print(c2e)
        # print(c2a)

    def test_load_csv6(self):

        c1e, c2e, c3e = create_data.make_csv_data(1000)
        c1a, c2a, c3a = program1.load_csv(os.path.join("data", "test_data.csv"))
        self.assertEqual(c1e, c1a, msg='data file has 1000 elements in first column!')
        for i in range(len(c2e)):
            self.assertAlmostEqual(c2e[i], c2a[i], msg='data file has 1000 elements in second column!')
            for i in range(len(c3e)):
                self.assertAlmostEqual(c3e[i], c3a[i], msg='data file has 1000 elements in third column!')


if __name__ == '__main__':
    unittest.main()
