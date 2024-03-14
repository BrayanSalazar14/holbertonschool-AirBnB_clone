from models import storage
from models.base_model import BaseModel
"""
Module in the User
"""


class User(BaseModel):
    """class User that inherits from BaseModel"""
    email = ""
    password = ""
    first_name = ""
    last_name = ""
