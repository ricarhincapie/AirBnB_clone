#!/usr/bin/python3
"""
Unit testing
"""

import unittest
from models.state import State
from models import state
import pep8


class TestPep8B(unittest.TestCase):
    """ Check for pep8 validation. """
    def test_pep8(self):
        """ test base and test_base for pep8 conformance """
        style = pep8.StyleGuide(quiet=True)
        file1 = 'models/state.py'
        file2 = 'tests/test_models/test_state.py'
        result = style.check_files([file1, file2])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warning).")


class TestDocsB(unittest.TestCase):
    """ Check for documentation. """
    def test_module_doc(self):
        """ check for module documentation """
        self.assertTrue(len(state.__doc__) > 0)

    def test_class_doc(self):
        """ check for documentation """
        self.assertTrue(len(state.__doc__) > 0)

    def test_method_docs(self):
        """ check for method documentation """
        for func in dir(State):
            self.assertTrue(len(func.__doc__) > 0)


class TestState(unittest.TestCase):
    """
    State class unit testing
    """
    def setUp(self):
        """
        Definign environment
        """
        self.state1 = State()

    def test_data_type(self):
        """
        Test data types
        """
        self.assertTrue(hasattr(self.state1, "name"))
        self.assertEqual(type(self.state1.name), str)

    def test_instantation(self):
        """
        Test instantation
        """
        self.assertIsInstance(self.state1, State)


if __name__ == "__main__":
    unittest.main()
