#!/usr/bin/python3
"""
Unit testing
"""

import unittest
from models.place import Place
from models import place
import pep8


class TestPep8B(unittest.TestCase):
    """ Check for pep8 validation. """
    def test_pep8(self):
        """ test base and test_base for pep8 conformance """
        style = pep8.StyleGuide(quiet=True)
        file1 = 'models/place.py'
        file2 = 'tests/test_models/test_place.py'
        result = style.check_files([file1, file2])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warning).")


class TestDocsB(unittest.TestCase):
    """ Check for documentation. """
    def test_module_doc(self):
        """ check for module documentation """
        self.assertTrue(len(place.__doc__) > 0)

    def test_class_doc(self):
        """ check for documentation """
        self.assertTrue(len(place.__doc__) > 0)

    def test_method_docs(self):
        """ check for method documentation """
        for func in dir(Place):
            self.assertTrue(len(func.__doc__) > 0)


class TestPlace(unittest.TestCase):
    """
    City class unit testing
    """
    def setUp(self):
        """
        Definign environment
        """
        self.place1 = Place()

    def test_data_type(self):
        """
        Test data types
        """
        self.assertTrue(hasattr(self.place1, "city_id"))
        self.assertEqual(type(self.place1.city_id), str)
        self.assertTrue(hasattr(self.place1, "user_id"))
        self.assertEqual(type(self.place1.user_id), str)
        self.assertTrue(hasattr(self.place1, "name"))
        self.assertEqual(type(self.place1.name), str)
        self.assertTrue(hasattr(self.place1, "description"))
        self.assertEqual(type(self.place1.description), str)
        self.assertTrue(hasattr(self.place1, "number_rooms"))
        self.assertEqual(type(self.place1.number_rooms), int)
        self.assertTrue(hasattr(self.place1, "number_bathrooms"))
        self.assertEqual(type(self.place1.number_bathrooms), int)
        self.assertTrue(hasattr(self.place1, "max_guest"))
        self.assertEqual(type(self.place1.max_guest), int)
        self.assertTrue(hasattr(self.place1, "price_by_night"))
        self.assertEqual(type(self.place1.price_by_night), int)
        self.assertTrue(hasattr(self.place1, "latitude"))
        self.assertEqual(type(self.place1.latitude), float)
        self.assertTrue(hasattr(self.place1, "longitude"))
        self.assertEqual(type(self.place1.longitude), float)
        self.assertTrue(hasattr(self.place1, "amenity_ids"))
        self.assertEqual(type(self.place1.amenity_ids), list)

    def test_instantation(self):
        """
        Test instantation
        """
        self.assertIsInstance(self.place1, Place)


if __name__ == "__main__":
    unittest.main()
