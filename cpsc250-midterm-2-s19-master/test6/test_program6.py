import unittest

from src6.program6 import Program6
from given.person import Person
from given.hero import Hero

from inspect import signature


class TestProgram6(unittest.TestCase):

    # ==========================================================================================================
    # Testing class Program6
    # ==========================================================================================================
    # -------------------------------------------------------------------------------------------------
    # Test if the function is defined.
    # -------------------------------------------------------------------------------------------------
    def test_init_method_exists(self):
        # -----------------------------------------------------
        # Hey, if you can read unit tests here's a big hint
        # -----------------------------------------------------
        method = '__init__'

        self.assertTrue(hasattr(Program6, method),
                        msg='{} in module {} does not exist'.format(method, "program6"))

        class_method = getattr(Program6, method)
        actual = len(signature(class_method).parameters)

        expected = 5  # Just self
        self.assertEqual(expected, actual,
                         msg='{} should take {} parameter(s) but it takes {}.'.format(
                             method, "program6", expected, actual)
                         )

    def test_str_method_exists(self):
        # -----------------------------------------------------
        # Hey, if you can read unit tests here's a big hint
        # -----------------------------------------------------
        method = '__str__'

        self.assertTrue(hasattr(Program6, method),
                        msg='{} in module {} does not exist'.format(method, "program6"))

        class_method = getattr(Program6, method)
        actual = len(signature(class_method).parameters)

        expected = 1  # Just self
        self.assertEqual(expected, actual,
                         msg='{} should take {} parameter(s) but it takes {}.'.format(
                             method, "program6", expected, actual)
                         )

    def test_inheritance(self):
        inst = Program6("Batman", 37, "no super power", "I'm Batman!")
        self.assertIsInstance(inst, Person, msg="Program6 must inherit from Person class")
        self.assertIsInstance(inst, Hero, msg="Program6 must inherit from Hero class")

    def test_name(self):
        inst = Program6("Batman", 37, "no super power", "I'm Batman!")
        self.assertEqual("Batman", inst.name, msg="Program6 must set name attribute")

    def test_age(self):
        inst = Program6("Batman", 37, "no super power", "I'm Batman!")
        self.assertEqual(37, inst.age, msg="Program6 must set age attribute")

    def test_super_power(self):
        inst = Program6("Batman", 37, "no super power", "I'm Batman!")
        self.assertEqual("no super power", inst.super_power, msg="Program6 must set super power attribute")

    def test_catch_phrase(self):
        inst = Program6("Batman", 37, "no super power", "I'm Batman!")
        self.assertEqual("I'm Batman!", inst.catch_phrase, msg="Program6 must set catch phrase attribute")

    def test_attributes(self):
        inst = Program6("Batman", 37, "no super power", "I'm Batman!")
        self.assertEqual("Batman", inst.name, msg="Program6 must set name attribute")
        self.assertEqual(37, inst.age, msg="Program6 must set age attribute")
        self.assertEqual("no super power", inst.super_power, msg="Program6 must set super power attribute")
        self.assertEqual("I'm Batman!", inst.catch_phrase, msg="Program6 must set catch phrase attribute")

    def test_str_contains(self):
        inst = Program6("Batman", 37, "no super power", "I'm Batman!")
        self.assertTrue("Batman" in str(inst), msg="Program6 string has name")
        self.assertTrue("37" in str(inst), msg="Program6 string has age")
        self.assertTrue("I'm Batman!" in str(inst), msg="Program6 string has catch phrase")  # don't care about capitals
        self.assertTrue("no super power" in str(inst), msg="Program6 string has super power")

    def test_str_contains_person(self):
        inst = Program6("Batman", 37, "no super power", "I'm Batman!")
        self.assertTrue(str(Person.__str__(inst)) in str(inst), msg="Program6 string has person string")

    def test_str_contains_hero(self):
        inst = Program6("Batman", 37, "no super power", "I'm Batman!")
        self.assertTrue(str(Hero.__str__(inst)) in str(inst), msg="Program6 string has hero string")


if __name__ == '__main__':
    unittest.main()
