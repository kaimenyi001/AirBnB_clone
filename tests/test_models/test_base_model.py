#!/usr/bin/python3
""" Module of Unittests for models/base_model.py """

import unittest
import models
from models.base_model import BaseModel
import os
from models.engine.file_storage import FileStorage
import datetime


class BaseModelTests(unittest.TestCase):
    """ Tests BaseModel """

    bm = BaseModel()

    def testBaseModel(self):
        """ Test attributes value of a BaseModel instance """

        self.bm.name = "Alx"
        self.bm.my_number = 89
        self.bm.save()
        my_json = self.bm.to_dict()

        self.assertEqual(self.bm.name, my_json['name'])
        self.assertEqual(self.bm.my_number, my_json['my_number'])
        self.assertEqual('BaseModel', my_json['__class__'])
        self.assertEqual(self.bm.id, my_json['id'])

    def testSave(self):
        """ Checks if the save method updates the public instance
        """
        self.bm.first_name = "First"
        self.bm.save()

        self.assertIsInstance(self.bm.id, str)
        self.assertIsInstance(self.bm.created_at, datetime.datetime)
        self.assertIsInstance(self.bm.updated_at, datetime.datetime)

        dict1 = self.bm.to_dict()

        self.bm.first_name = "Second"
        self.bm.save()
        dict2 = self.bm.to_dict()

        self.assertEqual(dict1['created_at'], dict2['created_at'])
        self.assertNotEqual(dict1['updated_at'], dict2['updated_at'])


if __name__ == '__main__':
    unittest.main()
