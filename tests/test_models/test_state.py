import unittest
from models.base_model import BaseModel
from models.state import State


class TestUser(unittest.TestCase):
    def setUp(self):
        self.model = State()

    def tearDown(self):
        del self.model

    def daughterClass(self):
        self.assertIsInstance(self.model, BaseModel)
        self.assertTrue(hasattr(self.model, "id"))
        self.assertTrue(hasattr(self.model, "created_at"))
        self.assertTrue(hasattr(self.model, "updated_at"))

    def test_atrr(self):
        my_state = self.model
        self.assertTrue(hasattr(my_state, "name"))

    def test_to_dict(self):
        my_state = self.model
        my_state.name = "***as"
        my_model_json = my_state.to_dict()
        attrs = ["id",
                 "created_at",
                 "updated_at",
                 "name",
                 "__class__"]
        self.assertCountEqual(my_model_json.keys(), attrs)
        self.assertEqual(my_model_json['__class__'], 'State')
        self.assertEqual(my_model_json['name'], "***as")

    def test_to_dict_values(self):
        format = "%Y-%m-%dT%H:%M:%S.%f"
        my_model = self.model
        my_model_json = my_model.to_dict()
        self.assertEqual(my_model_json["__class__"], "State")
        self.assertEqual(type(my_model_json["created_at"]), str)
        self.assertEqual(type(my_model_json["updated_at"]), str)
        self.assertNotEqual(my_model_json["created_at"],
                            my_model.created_at)
        self.assertNotEqual(my_model_json["updated_at"],
                            my_model.updated_at)
