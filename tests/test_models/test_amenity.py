#!/usr/bin/env python3
""" Unittest module for BaseModel class
"""

import unittest
import models
from models.amenity import Amenity


class TestAmenity(unittest.TestCase):
    """Test Amenity Class
    """
    def setUp(self):
        """setUp
        """
        self.am1 = Amenity()
        self.am2 = Amenity()

    def test_Amenity(self):
        """Test Amenity
        """
        self.assertNotEqual()

        self.assertNotEqual(self.bm1.id, self.bm2.id)
        self.assertEqual(self.bm1.__class__, self.bm2.__class__)
        bm1_dict = self.bm1.to_dict()
        self.assertIsInstance(bm1_dict, dict)
        bm1_str = self.bm1.__str__()
        self.assertIsInstance(bm1_str, str)
        update1 = self.bm1.updated_at
        self.bm1.save()
        update2 = self.bm1.updated_at
        self.assertNotEqual(update1, update2)
        str_bm1 = self.bm1.__str__()
        str_bm2 = self.bm2.__str__()
        self.assertNotEqual(str_bm1, str_bm2)
        my_str = "[{}] ({}) {}".format(self.bm1.__class__.__name__,
                                     self.bm1.id, self.bm1.__dict__)
        self.assertEqual(my_str, self.bm1.__str__())
                       
if __name__ == "__main__":
    unittest.main()
