#!/usr/bin/python3
"""
This is a module BaseModel
"""

import uuid
from datetime import datetime
import models

class BaseModel():
    """The BaseModel Class"""

    def __init__(self, *args, **kwargs):
        """This is a class constructor for the BaseModel Class"""

        if kwargs:
            kwargs['created_at'] = datetime.strptime(kwargs['created_at'],'%Y-%m-%dT%H:%M:%S.%f')
            kwargs['updated_at'] = datetime.strptime(kwargs['updated_at'],'%Y-%m-%dT%H:%M:%S.%f')

            for key, value in kwargs.items():
                if key != '__class__':
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.new(self)

    def __str__(self):
        """This is a string of BaseModel"""
        return "[{}] [{}] {}".format(self.__class__.__name__, self.id, self.__dict__)
    
    def save(self):
        """It updates 'updated_at' instance with the current datetime"""
        self.updated_at = datetime.now()
        models.save()

    def to_dict(self):
        """This is a dictionarry representation of an instance"""
        newdict = dict(self.__dict__)
        newdict["created_at"] = self.__dict__["created_at"].isoformat()
        newdict["updated_at"] = self.__dict__["updated_at"].isoformat()
        newdict["__class__"] = self.__class__.__name__

        return (newdict)
