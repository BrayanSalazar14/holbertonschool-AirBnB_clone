#!/usr/bin/python3
import unittest
import json
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel


classes = {"BaseModel": BaseModel}


class TestFileStorage(unittest.TestCase):
    def setUp(self):
        self.model = FileStorage()

    def tearDown(self):
        del self.model

    def testFilePath(self):
        self.assertEqual(self.model._FileStorage__file_path, "file.json")

    def test_all(self):
        new_dict = self.model.all()
        self.assertEqual(type(new_dict), dict)
        self.assertIs(new_dict, self.model._FileStorage__objects)

    def test_new(self):
        my_model = BaseModel()
        my_model.name = "My_First_Model"
        my_model.my_number = 89
        key = f"{my_model.__class__.__name__}.{my_model.id}"
        self.assertIn(key, self.model._FileStorage__objects, "No exists")

    def test_save(self):
        objs = {}
        save = FileStorage._FileStorage__objects
        FileStorage._FileStorage__objects = objs
        self.model.save()
        FileStorage._FileStorage__objects = save
        for key, value in objs.items():
            objs[key] = value.to_dict()
        file_json = json.dumps(objs)
        with open("file.json", "r") as file:
            file_read = file.read()
        self.assertEqual(json.loads(file_json), json.loads(file_read))
