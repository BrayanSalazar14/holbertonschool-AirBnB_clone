from models import storage
from models.base_model import BaseModel
"""
Module in the Review
"""


class Review(BaseModel):
    """Represents a review."""
    place_id = ""
    user_id = ""
    text = ""
