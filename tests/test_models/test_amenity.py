#!/usr/bin/python3
"""
 Defines Unittest for amenity.py
"""
import unittest
from models.amenity import Amenity
import datetime


class TestAmenity(unittest.TestCase):
    """Tests instances and methods from amenity class"""

    am = Amenity()

    def test_class_exists(self):
        """Tests if class exists"""
        res = "<class 'models.amenity.Amenity'>"
        self.assertEqual(str(type(self.am)), res)

    def test_user_inheritance(self):
        """Test if Amenity is a subclass of BaseModel"""
        self.assertIsInstance(self.am, Amenity)

    def testHasAttributes(self):
        """ Verify if attributes exist """
        self.assertTrue(hasattr(self.am, 'name'))
        self.assertTrue(hasattr(self.am, 'id'))
        self.assertTrue(hasattr(self.am, 'created_at'))
        self.assertTrue(hasattr(self.am, 'updated_at'))

    def test_types(self):
        """Tests if the type of the attribute is the correct one"""
        self.assertIsInstance(self.am.name, str)
        self.assertIsInstance(self.am.id, str)
        self.assertIsInstance(self.am.created_at, datetime.datetime)
        self.assertIsInstance(self.am.updated_at, datetime.datetime)


if __name__ == '__main__':
    unittest.main()
