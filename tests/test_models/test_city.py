#!/usr/bin/python3
"""
Unit testing
"""

import unittest
from models.city import City
from models import city
import pep8


class TestPep8B(unittest.TestCase):
    """ Check for pep8 validation. """
    def test_pep8(self):
        """ test base and test_base for pep8 conformance """
        style = pep8.StyleGuide(quiet=True)
        file1 = 'models/city.py'
        file2 = 'tests/test_models/test_city.py'
        result = style.check_files([file1, file2])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warning).")


class TestDocsB(unittest.TestCase):
    """ Check for documentation. """
    def test_module_doc(self):
        """ check for module documentation """
        self.assertTrue(len(city.__doc__) > 0)

    def test_class_doc(self):
        """ check for documentation """
        self.assertTrue(len(city.__doc__) > 0)

    def test_method_docs(self):
        """ check for method documentation """
        for func in dir(City):
            self.assertTrue(len(func.__doc__) > 0)


class TestCity(unittest.TestCase):
    """
    City class unit testing
    """
    def setUp(self):
        """
        Definign environment
        """
        self.city1 = City()

    def test_data_type(self):
        """
        Test data types
        """
        self.assertTrue(hasattr(self.city1, "name"))
        self.assertEqual(type(self.city1.name), str)
        self.assertTrue(hasattr(self.city1, "state_id"))
        self.assertEqual(type(self.city1.state_id), str)

    def test_instantation(self):
        """
        Test instantation
        """
        self.assertIsInstance(self.city1, City)


if __name__ == "__main__":
    unittest.main()
