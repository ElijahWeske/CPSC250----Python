import unittest
from inspect import signature

from src.farm_animal import FarmAnimal


class TestFarmAnimal(unittest.TestCase):
    class_name = "FarmAnimal"
    class_file = "farm_animal.py"
    class_class = FarmAnimal

    def test_farm_animal(self):
        fa = FarmAnimal(3.0)

        self.assertIsNotNone(fa)
        self.assertTrue(isinstance(fa,self.class_class))
        self.assertEqual(3.0,fa.age)

    def test_farm_animal_method(self):
        fa = FarmAnimal(1.0)

        self.assertIsNotNone(fa)
        self.assertIsInstance(fa, self.class_class,
                         msg='Should be instance of {}!'.format(self.class_name))
        expected = "" # empty string
        actual = fa.make_sound()
        self.assertEqual(expected, actual, msg='{}.{} should return {} parameter(s) but returns {} instead!'.format(self.class_name,
            "make_sound", expected, actual))
