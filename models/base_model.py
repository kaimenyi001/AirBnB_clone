#!/usr/bin/pyhon3
"""
Defines the BaseModel class
"""
import uuid
import models
from datetime import datetime


class BaseModel:
    """
    Defines all common attributes/methods
    """
    def __init__(self, *args, **kwargs):
        """
        Initializes all attributes
        """
        if not kwargs:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at
            models.storage.new(self)
        else:
            tf = "%Y-%m-%dT%H:%M:%S.%f"
            for key, val in kwargs.items():
                if key == 'created_at' or key == 'updated_at':
                    val = datetime.strptime(kwargs[key], tf)
                if key != '__class__':
                    setattr(self, key, val)

    def __str__(self):
        """
        Returns class name, id and attr dict
        """
        cls_nm = "[" + self.__class__.__name__ + "]"
        dicts = {ke: va for (ke, va) in self.
                 __dict__.items() if (not va) is False}
        return cls_nm + " (" + self.id + ") " + str(dicts)

    def save(self):
        """
        Updates time
        """
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """
        Return the dictionary of the BaseModel instance
        """
        n_dict = {}

        for key, vals in self.__dict__.items():
            if key == "created_at" or key == "updated_at":
                n_dict[key] = vals.strftime("%Y-%m-%dT%H:%M:%S.%f")
            else:
                if not vals:
                    pass
                else:
                    n_dict[key] = vals
        n_dict['__class__'] = self.__class__.__name__

        return n_dict
