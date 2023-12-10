#!/usr/bin/python3
"""This is Module for test User class"""
import unittest
import json
import pep8
import datetime

from models.user import User
from models.base_model import BaseModel


class TestUser(unittest.TestCase):
    """It Tests User class implementation"""
    def test_doc_module(self):
        """Module documentation"""
        my_doc = User.__doc__
        self.assertGreater(len(my_doc), 1)

    def test_pep8_conformance_base_model(self):
        """It Tests that models/user.py conforms to PEP8."""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/user.py'])
        self.assertEqual(result.total_errors, 0,
                         "Code style errors Found and warnings.")

    def test_pep8_conformance_test_base_model(self):
        """It Tests that tests/test_models/test_user.py conforms to PEP8."""
        pep8style = pep8.StyleGuide(quiet=True)
        result_2 = pep8style.check_files(['tests/test_models/test_user.py'])
        self.assertEqual(result_2.total_errors, 0,
                         "Code style errors Found and warnings.")

    def test_doc_constructor(self):
        """This is a Constructor documentation"""
        my_doc = User.__init__.__doc__
        self.assertGreater(len(my_doc), 1)

    def test_class(self):
        """It Validates the types of the attributes in a class"""
        with self.subTest(msg='Inheritance'):
            self.assertTrue(issubclass(User, BaseModel))

        with self.subTest(msg='Attributes'):
            self.assertIsInstance(User.user_email, str)
            self.assertIsInstance(User.user_password, str)
            self.assertIsInstance(User.first_name, str)
            self.assertIsInstance(User.last_name, str)


if __name__ == '__main__':
    unittest.main()
