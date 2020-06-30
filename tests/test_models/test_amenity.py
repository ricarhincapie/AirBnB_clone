#!/usr/bin/python3
"""
Unit testing
"""

import unittest
from models.amenity import Amenity
from models import amenity
import pep8


class TestPep8B(unittest.TestCase):
    """ Check for pep8 validation. """
    def test_pep8(self):
        """ test base and test_base for pep8 conformance """
        style = pep8.StyleGuide(quiet=True)
        file1 = 'models/amenity.py'
        file2 = 'tests/test_models/test_amenity.py'
        result = style.check_files([file1, file2])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warning).")


class TestDocsB(unittest.TestCase):
    """ Check for documentation. """
    def test_module_doc(self):
        """ check for module documentation """
        self.assertTrue(len(amenity.__doc__) > 0)

    def test_class_doc(self):
        """ check for documentation """
        self.assertTrue(len(amenity.__doc__) > 0)

    def test_method_docs(self):
        """ check for method documentation """
        for func in dir(Amenity):
            self.assertTrue(len(func.__doc__) > 0)


class TestAmenity(unittest.TestCase):
    """
    Amenity class unit testing
    """
    def setUp(self):
        """
        Definign environment
        """
        self.amenity1 = Amenity()

    def test_data_type(self):
        """
        Test data types
        """
        self.assertTrue(hasattr(self.amenity1, "name"))
        self.assertEqual(type(self.amenity1.name), str)

    def test_instantation(self):
        """
        Test instantation
        """
        self.assertIsInstance(self.amenity1, Amenity)


if __name__ == "__main__":
    unittest.main()
