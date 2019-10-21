import unittest
from inspect import signature

from src.farm_animal import FarmAnimal
from src.winged_animal import WingedAnimal
from src.duck import Duck


class TestDuck(unittest.TestCase):
    """
        Test Class for duck.py
    """
    class_name = "Duck"
    class_file = "duck.py"
    class_class = Duck

    def test_duck_class(self):
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


    def test_duck(self):
        rum = Duck(3.8)

        self.assertIsNotNone(rum)
        self.assertAlmostEqual(3.8, rum.age,
                         msg='The {} should set age attribute'.format(self.class_name))

        self.assertIsInstance(rum, self.class_class,
                         msg='Should be instance of {}!'.format(self.class_name))

        self.assertIsInstance(rum, WingedAnimal,
                         msg='Should be instance of {}!'.format("WingedAnimal"))

        self.assertIsInstance(rum, FarmAnimal,
                         msg='Should be instance of {}!'.format("FarmAnimal"))

    def test_duck_method(self):
        rum = self.class_class(1.0)

        self.assertIsNotNone(rum)
        self.assertIsInstance(rum, self.class_class,
                         msg='Should be instance of {}!'.format(self.class_name))
        expected = "flap, flap - quack, quack"

        actual = rum.make_sound()


        self.assertEqual(expected, actual, msg='{}.{} should return {} but returns {} instead!'.format(self.class_name,
            "make_sound", expected, actual))

    def test_duck_equal(self):
        self.assertTrue(Duck(1.1) == Duck(1.1), msg='Two {}s are equal if they are the same age'.format(self.class_name))
        self.assertFalse(Duck(1.1) == Duck(12.1), msg='Two {}s are equal if they are the same age'.format(self.class_name))

    def test_duck_not_equal_chicken(self):
        from src.chicken import  Chicken
        self.assertFalse(Duck(1.1) == Chicken(1.1), msg='Two different classes are not equal')

if __name__ == '__main__':
    unittest.main()
