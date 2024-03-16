#!/usr/bin/python3
import unittest
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel


class TestFileStorage(unittest.TestCase):
    def setUp(self):
        self.model = FileStorage()

    def tearDown(self):
        del self.model

    def test_all(self):
        new_dict = self.model.all()
        self.assertEqual(type(new_dict), dict)
