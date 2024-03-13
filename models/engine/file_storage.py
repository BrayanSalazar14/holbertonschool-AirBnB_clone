import json
from models.base_model import BaseModel


class FileStorage:
    __file_path = "file.json"
    __objects = {}

    def all(self):
        return self.__objects

    def new(self, obj):
        key = f"{obj.__class__.__name__}.{obj.id}"
        self.__objects[key] = obj

    def save(self):
        objs = {}
        for key, obj in self.__objects.items():
            objs[key] = obj.to_dict()

        with open(self.__file_path, mode="w", encoding="utf-8") as file:
            json.dump(objs, file)

    def reload(self):
        try:
            with open(self.__file_path, mode="r", encoding="utf-8") as file:
                for key, value in json.load(file).items():
                    obj = eval(value["__class__"])(**value)
                    self.__objects[key] = obj
        except FileNotFoundError:
            pass
