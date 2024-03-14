from models import storage
from models.base_model import BaseModel
"""
Module in the Place
"""


class Place(BaseModel):
    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    price_by_night = float(0)
    longitude = float(0)
    amenity_ids = []
