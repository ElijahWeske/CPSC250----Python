import unittest
from inspect import signature

from src.farm_animal import FarmAnimal
from src.winged_animal import WingedAnimal
from src.chicken import Chicken
from src.rooster import Rooster


class TestRooster(unittest.TestCase):
    """
        Test Class for rooster.py
    """
    class_name = "Rooster"
    class_file = "rooster.py"
    class_class = Rooster

    def test_rooster_class(self):
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


    def test_rooster(self):
        rum = Rooster(3.8)

        self.assertIsNotNone(rum)
        self.assertAlmostEqual(3.8, rum.age,
                         msg='The {} should set age attribute'.format(self.class_name))

        self.assertIsInstance(rum, self.class_class,
                         msg='Should be instance of {}!'.format(self.class_name))

        self.assertIsInstance(rum, Chicken,
                         msg='Should be instance of {}!'.format("Chicken"))

        self.assertIsInstance(rum, WingedAnimal,
                         msg='Should be instance of {}!'.format("WingedAnimal"))

        self.assertIsInstance(rum, FarmAnimal,
                         msg='Should be instance of {}!'.format("FarmAnimal"))

    def test_rooster_method(self):
        rooster = self.class_class(1.0)

        self.assertIsNotNone(rooster)
        self.assertIsInstance(rooster, self.class_class,
                         msg='Should be instance of {}!'.format(self.class_name))
        expected = "flap, flap - cock-a-doodle doo!"

        actual = rooster.make_sound()


        self.assertEqual(expected, actual, msg='{}.{} should return {} but returns {} instead!'.format(self.class_name,
            "make_sound", expected, actual))

if __name__ == '__main__':
    unittest.main()
