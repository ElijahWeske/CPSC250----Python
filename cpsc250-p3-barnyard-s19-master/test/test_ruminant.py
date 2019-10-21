import unittest
from inspect import signature

from src.farm_animal import FarmAnimal
from src.ruminant import Ruminant


class TestRuminant(unittest.TestCase):
    """
        Test Class for ruminant.py
    """
    class_name = "Ruminant"
    class_file = "ruminant.py"
    class_class = Ruminant

    def test_ruminant_class(self):
        method = 'make_sound'
        self.assertTrue(hasattr(self.class_class, method),
                        msg='The {} method in the {} class in {} does not exist'.format(method, self.class_name, self.class_file))
        expected = 1
        class_method = getattr(self.class_class, method)
        actual = len(signature(class_method).parameters)
        self.assertEqual(expected, actual,
                         msg='{}.{} should take {} parameter(s) but it takes {}. Does it have "self"?'.format(self.class_name,
                             method, expected, actual)
                         )


    def test_ruminant(self):
        rum = Ruminant(3.8)

        self.assertIsNotNone(rum)
        self.assertAlmostEqual(3.8, rum.age,
                         msg='The {} should set age attribute'.format(self.class_name))

        self.assertIsInstance(rum, self.class_class,
                         msg='Should be instance of {}!'.format(self.class_name))

        self.assertIsInstance(rum, FarmAnimal,
                         msg='Should be instance of {}!'.format("FarmAnimal"))

    def test_ruminant_method(self):
        rum = Ruminant(1.0)

        self.assertIsNotNone(rum)
        self.assertIsInstance(rum, self.class_class,
                         msg='Should be instance of {}!'.format(self.class_name))
        expected = "burp"
        actual = rum.make_sound()
        self.assertEqual(expected, actual, msg='{}.{} should return {} but returns {} instead!'.format(self.class_name,
            "make_sound", expected, actual))

if __name__ == '__main__':
    unittest.main()
