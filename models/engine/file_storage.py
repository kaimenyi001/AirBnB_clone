#!/usr/bin/python3

"""This is a file_storage.py module"""

import json
from models.base_model import BaseModel
from models.user import User
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State


class File_Storage():
    """File_Storage Class"""
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Public Instance Method that returns the
        dictionary __objects
        """

        return File_Storage.__objects

    def new(self, my_obj):
        """
        Public Instance Method That sets in __objects the
        obj with the Key <obj class name>.id
        Variables:

        Key [str] -- key format generated
        """

        if my_obj:
            key = "{}.{}".format(my_obj.__class__.__name__,  my_obj.id)
            File_Storage.__objects[key] = my_obj

    def save(self):
        """
        Public Instance Method that seralizes __objects to the
        JSON file (path: __file__path).
        Variables:

        new_dict [dict] - Keys and Values to build JSON
        """

        newdict = {}

        for key, value in File_Storage.__objects.items():
            newdict[key] = value.to_dict().copy()
        with open(File_Storage.__file_path, mode='w') as my_file:
            json.dump(newdict, my_file)

    def reload(self):
        """
        Piblic Instance Method That deserializes a JSON
        file to __objects.
        """

        try:
            with open(File_Storage.__file_path, mode='r') as my_file:
                newdict = json.load(my_file)

            for key, value in newdict.items():
                class_name = value.get('__class__')
                my_obj = eval(class_name + '(**value)')
                File_Storage.__objects[key] = my_obj

        except FileNotFoundError:
            pass
