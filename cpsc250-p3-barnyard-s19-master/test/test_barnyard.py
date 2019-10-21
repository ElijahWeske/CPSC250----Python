import unittest
from inspect import signature

from src.farm_animal import FarmAnimal
from src.winged_animal import WingedAnimal
from src.ruminant import Ruminant

from src.duck import Duck
from src.chicken import Chicken
from src.hen import Hen
from src.rooster import Rooster
from src.cow import Cow
from src.goat import Goat
from src import barnyard



class TestBarnyard(unittest.TestCase):
    """
        Test Class for barnyard.py
    """
    class_file = "barnyard.py"

    def test_get_barnyard_exists(self):
        method = 'get_barnyard'
        self.assertTrue(hasattr(barnyard, method),
                        msg='The {} method in the barnyard module in {} does not exist'.format(method, self.class_file))
        expected = 0
        class_method = getattr(barnyard, method)
        actual = len(signature(class_method).parameters)
        self.assertEqual(expected, actual,
                         msg='The {} method in {} should take {} parameter(s) but it takes {}. Does it have "self"?'.format(method, self.class_file, expected, actual)
                         )

    def test_get_layers_exists(self):
        method = 'get_layers'
        self.assertTrue(hasattr(barnyard, method),
                        msg='The {} method in the barnyard module in {} does not exist'.format(method, self.class_file))
        expected = 1
        class_method = getattr(barnyard, method)
        actual = len(signature(class_method).parameters)
        self.assertEqual(expected, actual,
                         msg='The {} method should take {} parameter(s) but it takes {}.'.format( method, expected, actual)
                         )

    def test_get_roosters_exists(self):
        method = 'get_roosters'
        self.assertTrue(hasattr(barnyard, method),
                        msg='The {} method in the barnyard module in {} does not exist'.format(method, self.class_file))
        expected = 1
        class_method = getattr(barnyard, method)
        actual = len(signature(class_method).parameters)
        self.assertEqual(expected, actual,
                         msg='The {} should take {} parameter(s) but it takes {}. '.format(method, expected, actual)
                         )

    def test_listen_exists(self):
        method = 'listen'
        self.assertTrue(hasattr(barnyard, method),
                        msg='The {} method in the barnyard module in {} does not exist'.format(method, self.class_file))
        expected = 1
        class_method = getattr(barnyard, method)
        actual = len(signature(class_method).parameters)
        self.assertEqual(expected, actual,
                         msg='The {} should take {} parameter(s) but it takes {}. '.format(  method, expected, actual)
                         )


    def test_get_list(self):
        animals = barnyard.get_barnyard()

        self.assertIsNotNone(animals,msg='barnyard.get_barnyard() should return a list of animals')
        self.assertIsInstance(animals,list, msg='barnyard.get_barnyard() should return a list of animals')

        self.assertTrue(len(animals) >= 10, msg="barnyard list requires at least 10 animals to meet spec")

    def test_list_contains(self):
        animals = barnyard.get_barnyard()

        types = [type(ani) for ani in animals]
        required = [Rooster, Hen, Duck, Goat, Cow]
        for req in required:
            self.assertTrue(req in types,msg='get_barnyard list must contain {}'.format(req))

        for ani in animals:
            self.assertIsInstance(ani ,FarmAnimal, msg='barnyard.get_barnyard() should return a list of only FarmAnimal type animals')

        required = [Hen(0.25), Hen(0.6), Hen(1.0), Hen(8),
               Rooster(0.25), Rooster(0.6), Rooster(1.0)]
        for req in required:
            self.assertTrue( req in animals, msg=' get_barnyard() list must contain at least one {}'.format(str(req)))

    def test_layers_contains(self):

        animals = [Hen(0.25), Hen(0.6), Hen(1.0), Hen(8),
                   Rooster(0.25), Rooster(0.6), Rooster(1.0), Cow(8.8)]

        layers = barnyard.get_layers(animals)
        expected = [Hen(0.6), Hen(1.0) ]

        for ex in expected:
            self.assertTrue(ex in layers,msg='given {} layers must contain {}'.format(animals, ex))

    def test_layers_contains2(self):

        animals = [Hen(0.25), Hen(0.6), Hen(1.0), Hen(3.0), Hen(8),
                   Rooster(0.25), Rooster(0.6), Rooster(1.0), Cow(8.8)]

        layers = barnyard.get_layers(animals)
        expected = [Hen(0.6), Hen(1.0), Hen(3.0)]

        for ex in expected:
            self.assertTrue(ex in layers, msg='given {} layers must contain {}'.format(animals, ex))

    def test_layers_contains3(self):

        animals = [Hen(0.25), Hen(8),
                   Rooster(0.25), Rooster(0.6), Rooster(1.0), Cow(8.8)]

        layers = barnyard.get_layers(animals)
        self.assertTrue(len(layers) == 0, msg='given {} layers must return empty list'.format(animals))

    def test_get_roosters(self):

        animals = [Hen(0.25), Hen(0.6), Hen(1.0), Hen(3.0), Hen(8),
                   Rooster(0.25), Rooster(0.6), Rooster(1.0), Cow(8.8)]

        roosters = barnyard.get_roosters(animals)
        expected = [Rooster(0.25), Rooster(0.6), Rooster(1.0)]

        for ex in expected:
            self.assertTrue(ex in roosters, msg='given {} roosters must contain {}'.format(animals, ex))

    def test_listen(self):

        animals = [Hen(0.25), Hen(0.6), Hen(1.0), Hen(3.0), Hen(8),
                   Rooster(0.25), Rooster(0.6), Rooster(1.0), Cow(8.8)]

        sounds = barnyard.listen(animals)
        expected = [Hen(0.25).make_sound(), Hen(0.6).make_sound(), Hen(1.0).make_sound(), Hen(3.0).make_sound(), Hen(8).make_sound(),
                   Rooster(0.25).make_sound(), Rooster(0.6).make_sound(), Rooster(1.0).make_sound(), Cow(8.8).make_sound()]

        self.assertEqual(expected, sounds, msg='given {} listen must contain {}'.format(animals, expected))

    def test_listen_unexpected(self):

        animals = [Hen(0.25), Hen(0.6), Hen(1.0), Hen(3.0), Hen(8),
                   Rooster(0.25), Rooster(0.6), Rooster(1.0), Cow(8.8)]

        sounds = barnyard.listen(animals+["This is not a FarmAnimal"])
        expected = [Hen(0.25).make_sound(), Hen(0.6).make_sound(), Hen(1.0).make_sound(), Hen(3.0).make_sound(), Hen(8).make_sound(),
                   Rooster(0.25).make_sound(), Rooster(0.6).make_sound(), Rooster(1.0).make_sound(), Cow(8.8).make_sound()]

        self.assertEqual(expected, sounds, msg='given {} listen must contain {}'.format(animals+["This is not a FarmAnimal"], expected))

        sounds = barnyard.listen(["This is not a FarmAnimal"]+animals)
        expected = [Hen(0.25).make_sound(), Hen(0.6).make_sound(), Hen(1.0).make_sound(), Hen(3.0).make_sound(), Hen(8).make_sound(),
                   Rooster(0.25).make_sound(), Rooster(0.6).make_sound(), Rooster(1.0).make_sound(), Cow(8.8).make_sound()]

        self.assertEqual(expected, sounds, msg='given {} listen must contain {}'.format(["This is not a FarmAnimal"]+animals, expected))


if __name__ == '__main__':
    unittest.main()
