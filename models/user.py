#!/usr/bin/python3

"""A Class that inherits from BaseModel"""

from models.base_model import BaseModel


class User(BaseModel):
    """Represents a Class User"""

    user_email = ""
    user_password = ""
    first_name = ""
    last_name = ""

    def __init__(self, *args, **kwargs):
        """Initializes The User Class"""
        super().__init__(*args, **kwargs)
