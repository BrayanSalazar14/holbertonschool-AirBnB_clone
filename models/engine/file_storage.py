import json
import os.path as path


class FileStorage:
    __file_path = "file.json"
    __objects = {}

    def all(self):
        return self.__objects

    def new(self, obj):
        key = f"{obj.__class__.__name__}.{obj.id}"
        self.__objects[key] = obj

    def save(self):
        object = {}
        for key, obj in self.__objects.items():
            object[key] = obj.to_dict()

        with open(self.__file_path, "w", encoding="utf-8") as file:
            json.dump(object, file)

    def reload(self):
        if path.exists(self.__file_path):
            with open(self.__file_path, "r", encoding="utf-8") as file:
                print("hi")
