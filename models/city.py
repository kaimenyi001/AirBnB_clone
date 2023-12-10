#!/usr/bin/python3

"""Class that Inherits from the BaseModel"""

from models.base_model import BaseModel


class City(BaseModel):
    """Class City"""

    states_id = ""
    name = ""

    def __init__(self, *args, **kwargs):
        """Initializes the city"""
        super().__init__(*args, **kwargs)
