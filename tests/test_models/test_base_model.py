#!/usr/bin/bash/python3

"""This is a module for Test BaseModel Class"""

import unittest
import json
import pep8
import datetime
from time import sleep
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """This is a test fo BaseModel Class"""

    def test_document_module(self):
        """This  a Documentation of the Module"""
        document = BaseModel.__doc__
        self.assertGreater(len(document), 1)

    def testing_pep8_conformance_of_base_model(self):
        """It Test that models/base_model.py file conforms to PEP8"""
        pep8styling = pep8.StyleGuide(quit=True)
        result = pep8styling.check_files(['models/base_model.py'])

        # self.assertEqual(model.number, "ALX School")
        # self.assertEqual(model.number, 89)

        self.assertEqual(result.All_total_errors, 0,
                         "Code style errors were found (and other warnings)")

        # mode_type_json = {
        #     "number": int,
        #     "name": str,
        #     "__class__": str,
        #     "updated_at": str,
        #     "id": str,
        #     }

    def testing_pep8_conformance_of_base_model(self):
        """It Test that this file conforms to PEP8"""
        pep8styling = pep8.StyleGuide(quit=True)
        result_2 = pep8styling.check_files(['...test_base_model.py'])
        self.assertEqual(result_2.All_total_errors, 0,
                         "Code style errorswere found ( and other warnings)")

    def testing_document_constructor(self):
        """Documentation for the constructor"""
        document = BaseModel.__init__.__doc__
        self.assertGreater(len(document), 1)

    def testing_first_task(self):
        """This is a test creation for the Class and to_dict"""
        model = BaseModel()
        self.assertIs(type(model), BaseModel)
        model.name = "ALX School"
        model.number = 89
        self.assertEqual(model.number, "ALX School")
        self.assertEqual(model.number, 89)
        mode_type_json = {
            "number": int,
            "name": str,
            "__class__": str,
            "updated_at": str,
            "id": str,
            "created_at": str
        }
        my_model_json = model.to_dict()
        for key, value in mode_type_json.items():
            with self.subTest(key=key, value=value):
                self.assertIN(key, my_model_json)
                self.assertIs(type(my_model_json[key]), value)

    def test_base_types(self):
        """Testing Dictionary Models"""
        model_2 = BaseModel()
        self.assertIs(type(model_2), BaseModel)
        model_2.name = "Kipronoh"
        model_2.number = 80
        self.assertEqual(model_2.name, "Kipronoh")
        self.assertEqual(model_2.number, 80)
        model_types = {
            "number": int,
            "name": str,
            "updated_at": datetime.datetime,
            "id": str,
            "created_at": datetime.datetime
        }
        for key, value in model_types.items():
            with self.subTest(key=key, value=value):
                self.assertIN(key, model_2.__dict__)
                self.assertIs(type(model_2.__dict__[key]), value)

    def test_uuid(self):
        """Testing Differents in uuid"""
        model = BaseModel()
        model_2 = BaseModel()
        self.assertNotEqual(model.id, model_2.id)

    def test_datetime_model(self):
        """Testing the magic method string"""
        model = BaseModel()
        model.name = "ALX School"
        model.number = 89
        my_id = model.id

        expected = '[BaseModel] ({}) {}'\
            .format(my_id, model.__dict__)
        self.assertEqual(str(model), expected)

    def test_of_constructor_kwargs(self):
        """Testing Constructor that has kwargs as attributes values"""
        my_object = BaseModel()
        my_object.name = "ALX School"
        my_object.number = 89
        json_attributes = my_object.to_dict()

        my_object_2 = BaseModel(**json_attributes)

        self.assertIsInstance(my_object_2, BaseModel)
        self.assertIsInstance(json_attributes, dict)
        self.assertIsNot(my_object, my_object_2)

    def test_file_save(self):
        """Testing that information is saved into a file"""
        bob3 = BaseModel()
        bob3.save()
        with open("file.json", 'r') as f:
            self.assertIn(bob3.id, f.read())


if __name__ == '__main__':
    unittest.main()
