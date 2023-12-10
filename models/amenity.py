#!/usr/bin/python3

"""Class That inherits from the BaseModel"""

from models.base_model import BaseModel


class Amenity(BaseModel):
    """Class Amenity"""

    name = ""

    def __init__(self, *args, **kwargs):
        """Initializes Amenityy"""
        super().__init__(*args, **kwargs)
