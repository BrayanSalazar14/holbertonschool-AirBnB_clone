import uuid
import datetime
"""
Module that defines all common attributes/methods for other classes
"""


class BaseModel:
    def __init__(self):
        self.id = str(uuid.uuid4())
        self.created_at = datetime.datetime.now()
        self.updated_at = datetime.datetime.now()

    def __str__(self):
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        self.updated_at = datetime.datetime.now()

    def to_dict(self):
        obj_dictionary = self.__dict__.copy()
        obj_dictionary["__class__"] = self.__class__.__name__
        obj_dictionary["created_at"] = self.created_at.isoformat()
        obj_dictionary["update_at"] = self.updated_at.isoformat()
        return obj_dictionary
