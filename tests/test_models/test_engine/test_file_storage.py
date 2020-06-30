#!/usr/bin/python3
""" Unittest module for BaseModel class
"""
import pep8
import unittest
from models.base_model import BaseModel
from models.engine import file_storage
from models.engine.file_storage import FileStorage


class TestPep8B(unittest.TestCase):
    """ Check for pep8 validation. """
    def test_pep8(self):
        """ test base and test_base for pep8 conformance """
        style = pep8.StyleGuide(quiet=True)
        file1 = 'models/engine/file_storage.py'
        file2 = 'tests/test_models/test_engine/test_file_storage.py'
        result = style.check_files([file1, file2])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warning).")


class TestDocsB(unittest.TestCase):
    """ Check for documentation. """
    def test_module_doc(self):
        """ check for module documentation """
        self.assertTrue(len(file_storage.__doc__) > 0)

    def test_class_doc(self):
        """ check for documentation """
        self.assertTrue(len(file_storage.__doc__) > 0)

    def test_method_docs(self):
        """ check for method documentation """
        for func in dir(FileStorage):
            self.assertTrue(len(func.__doc__) > 0)


class TestFileEstorage(unittest.TestCase):
    """ Check for functionality of File_Storage class. """
    def setUp(self):
        """ Method to set the star point. """
        self.fs = FileStorage()

    def test_all(self):
        """ Test if the method return a dictionary correctly. """
        my_dict = self.fs.all()
        self.assertEqual(type(my_dict), dict)

    def test_instantation(self):
        """ Check if a variable is an instance. """
        self.assertIsInstance(self.fs, FileStorage)


if __name__ == "__main__":
    unittest.main()
