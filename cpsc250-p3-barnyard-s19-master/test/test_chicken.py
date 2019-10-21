import unittest
from inspect import signature

from src.farm_animal import FarmAnimal
from src.winged_animal import WingedAnimal
from src.chicken import Chicken


class TestChicken(unittest.TestCase):
    """
        Test Class for chicken.py
    """
    class_name = "Chicken"
    class_file = "chicken.py"
    class_class = Chicken

    def test_chicken_class(self):
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


    def test_chicken(self):
        rum = Chicken(3.8)

        self.assertIsNotNone(rum)
        self.assertAlmostEqual(3.8, rum.age,
                         msg='The {} should set age attribute'.format(self.class_name))

        self.assertIsInstance(rum, self.class_class,
                         msg='Should be instance of {}!'.format(self.class_name))

        self.assertIsInstance(rum, WingedAnimal,
                         msg='Should be instance of {}!'.format("WingedAnimal"))

        self.assertIsInstance(rum, FarmAnimal,
                         msg='Should be instance of {}!'.format("FarmAnimal"))

    def test_chicken_method(self):
        rum = self.class_class(1.0)

        self.assertIsNotNone(rum)
        self.assertIsInstance(rum, self.class_class,
                         msg='Should be instance of {}!'.format(self.class_name))
        expected = "flap, flap - cluck, cluck"

        actual = rum.make_sound()


        self.assertEqual(expected, actual, msg='{}.{} should return {} but returns {} instead!'.format(self.class_name,
            "make_sound", expected, actual))

    def test_chicken_equal(self):
        self.assertTrue(Chicken(1.1) == Chicken(1.1), msg='Two {}s are equal if they are the same age'.format(self.class_name))
        self.assertFalse(Chicken(1.1) == Chicken(12.1), msg='Two {}s are equal if they are the same age'.format(self.class_name))

if __name__ == '__main__':
    unittest.main()
