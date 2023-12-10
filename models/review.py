#!/usr/bin/python3

"""Class that inherits from the BaseModel"""

from models.base_model import BaseModel


class Review(BaseModel):
    """Class Review"""

    place_id = ""
    user_id = ""
    text = ""

    def __init__(self, *args, **kwargs):
        """It initialixes Review"""
        super().__init__(*args, **kwargs)
