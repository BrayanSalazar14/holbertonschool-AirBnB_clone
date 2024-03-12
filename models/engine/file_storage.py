import json
from models.base_model import BaseModel

classes = {"BaseModel": BaseModel}


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

        with open(self.__file_path, "w", encoding="utf-8") as file:
            json.dump(objs, file)

    def reload(self):
        try:
            with open(self.__file_path, "r", encoding="utf-8") as file:
                f = json.load(file)
                for key in f:
                    self.__objects[key] = classes[f[key]
                                                  ["__class__"]](**f[key])
        except FileNotFoundError:
            pass
