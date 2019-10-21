import unittest
from inspect import signature

from src.farm_animal import FarmAnimal
from src.ruminant import Ruminant
from src.cow import Cow


class TestCow(unittest.TestCase):
    """
        Test Class for cow.py
    """
    class_name = "Cow"
    class_file = "cow.py"
    class_class = Cow

    def test_cow_class(self):
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


    def test_cow(self):
        rum = Cow(3.8)

        self.assertIsNotNone(rum)
        self.assertAlmostEqual(3.8, rum.age,
                         msg='The {} should set age attribute'.format(self.class_name))

        self.assertIsInstance(rum, self.class_class,
                         msg='Should be instance of {}!'.format(self.class_name))

        self.assertIsInstance(rum, Ruminant,
                         msg='Should be instance of {}!'.format("Ruminant"))

        self.assertIsInstance(rum, FarmAnimal,
                         msg='Should be instance of {}!'.format("FarmAnimal"))

    def test_cow_method(self):
        rum = self.class_class(1.0)

        self.assertIsNotNone(rum)
        self.assertIsInstance(rum, self.class_class,
                         msg='Should be instance of {}!'.format(self.class_name))
        expected1 = "burp - moo"
        expected2 = "Eat mor chikin!"

        actual = rum.make_sound()


        self.assertTrue(expected1 == actual or expected2 == actual, msg='{}.{} should return {} or {} but returns {} instead!'.format(self.class_name,
            "make_sound", expected1, expected2, actual))

    def test_cow_equal(self):
        self.assertTrue(Cow(1.1) == Cow(1.1), msg='Two {}s are equal if they are the same age'.format(self.class_name))
        self.assertFalse(Cow(1.1) == Cow(12.1), msg='Two {}s are equal if they are the same age'.format(self.class_name))

if __name__ == '__main__':
    unittest.main()
