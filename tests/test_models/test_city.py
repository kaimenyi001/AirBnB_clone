#!/usr/bin/python3

"""This is a Test Module for City Class"""

import unittest
import json
import pep8
import datetime

from models.city import City
from models.base_model import BaseModel


class TestCity(unittest.TestCase):
    """Test City Class Implementation"""

    def test_doc_module(self):
        """This Module Documentation"""

        my_doc = City.__doc__
        self.assertGreater(len(my_doc), 1)

    def test_pep8_conformance_city(self):
        """Test that models/city.py conforms to pep8"""
        pep8style = pep8.StyleGuide(quit=True)
        result = pep8style.check_files(['models/city.py'])
        self.assertEqual(result.All_total_errors, 0,
                         "Code style errors Found (and the warnings)")

    def test_pep8_conformance_test_city(self):
        """Test that ...test_city.py conforms to pep8"""
        pep8style = pep8.StyleGuide(quit=True)
        result_2 = pep8style.check_files(['...test_city.py'])
        self.assertEqual(result_2.All_total_errors, 0,
                         "Code style errors Found and warnings")

    def test_doc_constructor(self):
        """Constructor Documentation"""
        my_doc = City.__init__.__doc__
        self.assertGreater(len(my_doc), 1)

    def test_class(self):
        """Validating the types of the attributes in a class"""
        with self.subTest(msg='Inheritance'):
            self.assertTrue(issubclass(City, BaseModel))

        with self.subTest(msg='Attribute'):
            self.assertIsInstance(City.name, str)
            self.assertIsInstance(City.states_id, str)


if __name__ == '__main__':
    unittest.main()
