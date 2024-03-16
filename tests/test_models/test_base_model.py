#!/usr/bin/python3
import unittest
import json
from models.base_model import BaseModel
from tests.test_models.test_engine import test_file_storage
from models import storage


class TestBaseModel(unittest.TestCase):

    def setUp(self):
        self.model = BaseModel()

    def tearDown(self):
        del self.model

    def test_atrributes(self):
        self.model.name = "Brayan"
        self.model.age = 21
        self.assertEqual(self.model.name, "Brayan")
        self.assertEqual(self.model.age, 21)

    def test_str(self):
        class_name = self.model.__class__.__name__
        output = f"[{class_name}] ({self.model.id}) {str(self.model.__dict__)}"
        self.assertEqual(output, self.model.__str__())

    def test_to_dict(self):
        my_model = BaseModel()
        my_model.name = "My First Model"
        my_model.my_number = 89
        my_model_json = my_model.to_dict()
        attrs = ["id",
                 "created_at",
                 "updated_at",
                 "name",
                 "my_number",
                 "__class__"]
        self.assertCountEqual(my_model_json.keys(), attrs)
        self.assertEqual(my_model_json['__class__'], 'BaseModel')
        self.assertEqual(my_model_json['name'], "My First Model")
        self.assertEqual(my_model_json['my_number'], 89)

    def test_to_dict_values(self):
        format = "%Y-%m-%dT%H:%M:%S.%f"
        my_model = self.model
        my_model_json = my_model.to_dict()
        self.assertEqual(my_model_json["__class__"], "BaseModel")
        self.assertEqual(type(my_model_json["created_at"]), str)
        self.assertEqual(type(my_model_json["updated_at"]), str)
        self.assertNotEqual(my_model_json["created_at"],
                            my_model.created_at)
        self.assertNotEqual(my_model_json["updated_at"],
                            my_model.updated_at)

    def test_save(self):
        new_dict = {}
        instance = self.model
        instance_key = instance.__class__.__name__ + "." + instance.id
        new_dict[instance_key] = instance
        save = storage._FileStorage__objects
        storage._FileStorage__objects = new_dict
        storage.save()
        storage._FileStorage__objects = save
        for key, value in new_dict.items():
            new_dict[key] = value.to_dict()
        file_json = json.dumps(new_dict)
        with open("file.json", "r", encoding="utf-8") as file:
            file_read = file.read()
        self.assertEqual(json.loads(file_json), json.loads(file_read))
