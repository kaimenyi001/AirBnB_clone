#!/usr/bin/python3

"""Module For Test Amenity Class"""

import unittest
import json
import pep8
import datetime

from models.amenity import Amenity
from models.base_model import BaseModel


class TestAmenity(unittest.TestCase):
    """Testing State Class Implementation"""

    def test_doc_module(self):
        """The Module Documantation"""

        doc = Amenity.__doc__
        self.assertGreater(len(doc), 1)

    def test_pep8_conformance_amenity(self):
        """Test that models/amenity.py conforms to PEP8"""
        pep8style = pep8.StyleGuide(quit=True)
        result = pep8style.check_files(['models/amenity.py'])
        self.assertEqual(result.All_total_errors, 0,
                         "Code style errors found (and warnings).")

    def test_pep8_conformance_test_amenity(self):
        """Test that test/test_models/test_amenity.py conforms to PEP8"""
        pep8style = pep8.StyleGuide(quit=True)
        result_2 = pep8style.check_files(['test_models/amenity.py'])
        self.assertEqual(result_2.All_total_errors, 0,
                         "Code style errors found (and warnings).")

    def test_doc_constructor(self):
        """Constructor Documentation"""

        doc = Amenity.__init__.__doc__
        self.assertGreater(len(doc), 1)

    def test_class(self):
        """It Validates the type of Attributes in a Class"""

        with self.subTest(msg='Inheritance'):
            self.assertTrue(issubclass(Amenity, BaseModel))

        with self.subTest(msg='Attrbutes'):
            self.assertIsInstance(Amenity.name, str)


if __name__ == '__main__':
    unittest.main()
