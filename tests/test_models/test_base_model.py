#!/usr/bin/python3
import unittest
from datetime import datetime
import os
from models.base_model import BaseModel


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
