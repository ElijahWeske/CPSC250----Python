import unittest
from inspect import signature

from src.farm_animal import FarmAnimal
from src.winged_animal import WingedAnimal


class TestWingedAnimal(unittest.TestCase):
    """
        Test Class for winged_animal.py
    """
    class_name = "WingedAnimal"
    class_file = "winged_animal.py"
    class_class = WingedAnimal

    def test_winged_animal_class(self):
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


    def test_winged_animal(self):
        wa = WingedAnimal(1.2)

        self.assertIsNotNone(wa)
        self.assertAlmostEqual(1.2, wa.age,
                         msg='The {} should set age attribute'.format(self.class_name))

        self.assertIsInstance(wa, self.class_class,
                         msg='Should be instance of {}!'.format(self.class_name))
        self.assertIsInstance(wa, FarmAnimal,
                         msg='Should be instance of {}!'.format("FarmAnimal"))


    def test_winged_animal_method(self):
        wa = WingedAnimal(1.0)

        self.assertIsNotNone(wa)
        self.assertIsInstance(wa, self.class_class,
                         msg='Should be instance of {}!'.format(self.class_name))
        expected = "flap, flap"
        actual = wa.make_sound()
        self.assertEqual(expected, actual, msg='{}.{} should return {} but returns {} instead!'.format(self.class_name,
            "make_sound", expected, actual))

if __name__ == '__main__':
    unittest.main()
