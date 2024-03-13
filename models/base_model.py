import uuid
from models import storage
from datetime import datetime
"""
Module that defines all common attributes/methods for other classes
"""


class BaseModel:
    def __init__(self, *args, **kwargs):
        if not kwargs:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at
            storage.new(self)
            return
        for key, value in kwargs.items():
            if key == "__class__":
                continue
            if key == "created_at" or key == "updated_at":
                self.__dict__[key] = datetime.strptime(
                    value, "%Y-%m-%dT%H:%M:%S.%f")
            else:
                self.__dict__[key] = value
        # for key, value in kwargs.items():
        #     if key != "__class__":
        #         setattr(self, key, value)
        #     if key == "created_at" or key == "updated_at":
        #         value = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")

    def __str__(self):
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        obj_dictionary = self.__dict__.copy()
        obj_dictionary["__class__"] = self.__class__.__name__
        obj_dictionary["created_at"] = self.created_at.isoformat()
        obj_dictionary["updated_at"] = self.updated_at.isoformat()
        return obj_dictionary
