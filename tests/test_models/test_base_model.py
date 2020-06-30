#!/usr/bin/python3
""" Unittest module for BaseModel class
"""

import unittest
import models
from models.base_model import BaseModel
from models import base_model
import pep8


class TestPep8B(unittest.TestCase):
    """ Check for pep8 validation. """
    def test_pep8(self):
        """ test base and test_base for pep8 conformance """
        style = pep8.StyleGuide(quiet=True)
        file1 = 'models/base_model.py'
        file2 = 'tests/test_models/test_base_model.py'
        result = style.check_files([file1, file2])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warning).")


class TestDocsB(unittest.TestCase):
    """ Check for documentation. """
    def test_module_doc(self):
        """ check for module documentation """
        self.assertTrue(len(base_model.__doc__) > 0)

    def test_class_doc(self):
        """ check for documentation """
        self.assertTrue(len(BaseModel.__doc__) > 0)

    def test_method_docs(self):
        """ check for method documentation """
        for func in dir(BaseModel):
            self.assertTrue(len(func.__doc__) > 0)


class TestBaseModel(unittest.TestCase):
    """
    Test Base Model
    """
    def setUp(self):
        """
        setUp
        """
        arguments = {
            "updated_at": "2020-06-29T20:13:30.925617",
            "id": "44367831-eb30-415e-b395-3aeefab79f12",
            "created_at": "2020-06-29T20:13:30.925458",
            "__class__": "BaseModel"
            }
        self.bm1 = BaseModel()
        self.bm2 = BaseModel(**arguments)

    def tearDown(self):
        """
        tear down
        """
        del self.bm1
        del self.bm2

    def test_to_dict(self):
        """
        test to_dict function
        """
        bm2_dict = self.bm2.to_dict()
        ductionary = {
            'updated_at': '2020-06-29T20:13:30.925617',
            'id': '44367831-eb30-415e-b395-3aeefab79f12',
            'created_at': '2020-06-29T20:13:30.925458',
            '__class__': 'BaseModel'
            }
        self.assertIsInstance(bm2_dict, dict)
        self.assertEqual(bm2_dict, ductionary)

    def test_id(self):
        """ Check if id of a instance is a string or equal to another one. """
        self.assertNotEqual(self.bm1.id, self.bm2.id)
        self.assertEqual(type(self.bm1.id), str)

    def test_str(self):
        """
        test str function
        """
        bm2_str = str(self.bm2)
        my_str = "[{}] ({}) {}".format(self.bm2.__class__.__name__,
                                       self.bm2.id, self.bm2.__dict__)
        self.assertIsInstance(bm2_str, str)
        self.assertEqual(bm2_str, my_str)

    def test_save(self):
        """
        Test method save
        """
        update1 = self.bm1.updated_at
        self.bm1.save()
        update2 = self.bm1.updated_at
        self.assertNotEqual(update1, update2)

    def test_instantation(self):
        """Test BaseModel
        """
        self.assertIsInstance(self.bm1, BaseModel)
        self.assertTrue(hasattr(self.bm1, "updated_at"))
        self.assertTrue(hasattr(self.bm1, "created_at"))
        self.assertTrue(hasattr(self.bm1, "id"))


if __name__ == "__main__":
    unittest.main()
