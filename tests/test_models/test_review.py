#!/usr/bin/python3
"""This is a Module for test Review class"""
import unittest
import json
import pep8
import datetime

from models.review import Review
from models.base_model import BaseModel


class TestReview(unittest.TestCase):
    """This is a Test Review class implementation"""
    def test_doc_module(self):
        """This a Module documentation"""
        doc = Review._doc_
        self.assertGreater(len(doc), 1)

    def test_pep8_conformance_review(self):
        """This Tests that models/review.py conforms to PEP8."""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/review.py'])
        self.assertEqual(result.total_errors, 0,
                         "Code style errors Found and warnings.")

    def test_pep8_conformance_test_review(self):
        """Tests that tests/test_models/test_review.py conforms to PEP8."""
        pep8style = pep8.StyleGuide(quiet=True)
        result_2 = pep8style.check_files(['tests/test_models/test_review.py'])
        self.assertEqual(result_2.total_errors, 0,
                         "Code style errors Found and warnings.")

    def test_doc_constructor(self):
        """Constructor documentation"""
        my_doc = Review._init.doc_
        self.assertGreater(len(my_doc), 1)

    def test_class(self):
        """Validate the types of the attributes a class"""
        with self.subTest(msg='Inheritance'):
            self.assertTrue(issubclass(Review, BaseModel))

        with self.subTest(msg='Attributes'):
            self.assertIsInstance(Review.place_id, str)
            self.assertIsInstance(Review.user_id, str)
            self.assertIsInstance(Review.text, str)


if __name__ == '__main__':
    unittest.main()
