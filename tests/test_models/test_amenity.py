import unittest
from models.base_model import BaseModel
from models.amenity import Amenity


class TestUser(unittest.TestCase):
    def setUp(self):
        self.model = Amenity()

    def tearDown(self):
        del self.model

    def daughterClass(self):
        self.assertIsInstance(self.model, BaseModel)
        self.assertTrue(hasattr(self.model, "id"))
        self.assertTrue(hasattr(self.model, "created_at"))
        self.assertTrue(hasattr(self.model, "updated_at"))

    def test_atrr(self):
        my_amenity = self.model
        self.assertTrue(hasattr(my_amenity, "name"))

    def test_to_dict(self):
        my_amenity = self.model
        my_amenity.name = "***as"
        my_model_json = my_amenity.to_dict()
        attrs = ["id",
                 "created_at",
                 "updated_at",
                 "name",
                 "__class__"]
        self.assertCountEqual(my_model_json.keys(), attrs)
        self.assertEqual(my_model_json['__class__'], 'Amenity')
        self.assertEqual(my_model_json['name'], "***as")

    def test_to_dict_values(self):
        format = "%Y-%m-%dT%H:%M:%S.%f"
        my_model = self.model
        my_model_json = my_model.to_dict()
        self.assertEqual(my_model_json["__class__"], "Amenity")
        self.assertEqual(type(my_model_json["created_at"]), str)
        self.assertEqual(type(my_model_json["updated_at"]), str)
        self.assertNotEqual(my_model_json["created_at"],
                            my_model.created_at)
        self.assertNotEqual(my_model_json["updated_at"],
                            my_model.updated_at)
