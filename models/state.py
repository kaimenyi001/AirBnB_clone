#!/usr/bin/python3

"""Class that inherits from BaseModel"""

from models.base_model import BaseModel


class State(BaseModel):
    """State Class"""

    name = ""

    def __init__(self, *args, **kwargs):
        """Initializes the State class"""
        super().__init__(*args, **kwargs)
