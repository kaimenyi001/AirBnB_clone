#!/usr/bin/python3

"""It inherits from the BaseModel"""

from models.base_model import BaseModel


class Place(BaseModel):
    """Class Place"""

    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_of_rooms = ""
    number_of_bathrooms = ""
    max_no_of_guest = ""
    latitude = ""
    longitude = ""
    amenity_id = ""

    def __init__(self, *args, **kwargs):
        """Initializes Place"""
        super().__init__(*args, **kwargs)
