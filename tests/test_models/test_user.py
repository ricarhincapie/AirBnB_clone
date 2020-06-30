#!/usr/bin/python3
"""
Unit testing
"""

import unittest
from models.user import User
from models import user
import pep8


class TestPep8B(unittest.TestCase):
    """ Check for pep8 validation. """
    def test_pep8(self):
        """ test base and test_base for pep8 conformance """
        style = pep8.StyleGuide(quiet=True)
        file1 = 'models/user.py'
        file2 = 'tests/test_models/test_user.py'
        result = style.check_files([file1, file2])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warning).")


class TestDocsB(unittest.TestCase):
    """ Check for documentation. """
    def test_module_doc(self):
        """ check for module documentation """
        self.assertTrue(len(user.__doc__) > 0)

    def test_class_doc(self):
        """ check for documentation """
        self.assertTrue(len(user.__doc__) > 0)

    def test_method_docs(self):
        """ check for method documentation """
        for func in dir(User):
            self.assertTrue(len(func.__doc__) > 0)


class TestState(unittest.TestCase):
    """
    State class unit testing
    """
    def setUp(self):
        """
        Definign environment
        """
        self.user1 = User()

    def test_data_type(self):
        """
        Test data types
        """
        self.assertTrue(hasattr(self.user1, "email"))
        self.assertEqual(type(self.user1.email), str)

        self.assertTrue(hasattr(self.user1, "password"))
        self.assertEqual(type(self.user1.password), str)

        self.assertTrue(hasattr(self.user1, "first_name"))
        self.assertEqual(type(self.user1.first_name), str)

        self.assertTrue(hasattr(self.user1, "last_name"))
        self.assertEqual(type(self.user1.last_name), str)

    def test_instantation(self):
        """
        Test instantation
        """
        self.assertIsInstance(self.user1, User)


if __name__ == "__main__":
    unittest.main()
