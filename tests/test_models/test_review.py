#!/usr/bin/python3
"""
Unit testing
"""

import unittest
from models.review import Review
from models import review
import pep8


class TestPep8B(unittest.TestCase):
    """ Check for pep8 validation. """
    def test_pep8(self):
        """ test base and test_base for pep8 conformance """
        style = pep8.StyleGuide(quiet=True)
        file1 = 'models/review.py'
        file2 = 'tests/test_models/test_review.py'
        result = style.check_files([file1, file2])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warning).")


class TestDocsB(unittest.TestCase):
    """ Check for documentation. """
    def test_module_doc(self):
        """ check for module documentation """
        self.assertTrue(len(review.__doc__) > 0)

    def test_class_doc(self):
        """ check for documentation """
        self.assertTrue(len(review.__doc__) > 0)

    def test_method_docs(self):
        """ check for method documentation """
        for func in dir(Review):
            self.assertTrue(len(func.__doc__) > 0)


class TestReview(unittest.TestCase):
    """
    Amenity class unit testing
    """
    def setUp(self):
        """
        Definign environment
        """
        self.review1 = Review()

    def test_data_type(self):
        """
        Test data types
        """
        self.assertTrue(hasattr(self.review1, "place_id"))
        self.assertEqual(type(self.review1.place_id), str)
        self.assertTrue(hasattr(self.review1, "user_id"))
        self.assertEqual(type(self.review1.user_id), str)
        self.assertTrue(hasattr(self.review1, "text"))
        self.assertEqual(type(self.review1.text), str)

    def test_instantation(self):
        """
        Test instantation
        """
        self.assertIsInstance(self.review1, Review)


if __name__ == "__main__":
    unittest.main()
