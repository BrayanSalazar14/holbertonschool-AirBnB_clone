import unittest
from models.base_model import BaseModel
from models.user import User


class TestUser(unittest.TestCase):
    def setUp(self):
        self.model = User()

    def tearDown(self):
        del self.model

    def test_attr(self):
        user = self.model
        self.assertTrue(hasattr(user, "email"))
        self.assertTrue(hasattr(user, "password"))
        self.assertTrue(hasattr(user, "first_name"))
        self.assertTrue(hasattr(user, "last_name"))

    def test_email(self):
        self.assertTrue(hasattr(self.model, "email"))
        email = "bsalazarperdomo@gmail.com"
        user = User(email=email)
        self.assertEqual(user.email, email)

    def test_password(self):
        password = "***a"
        user = User(password=password)
        self.assertEqual(user.password, password)

    def test_first_name(self):
        first_name = "Brayan"
        user = User(first_name=first_name)
        self.assertEqual(user.first_name, first_name)

    def test_last_name(self):
        last_name = "Steven"
        user = User(last_name=last_name)
        self.assertEqual(user.last_name, last_name)

    def daughterClass(self):
        self.assertIsInstance(self.model, BaseModel)
        self.assertTrue(hasattr(self.model, "id"))
        self.assertTrue(hasattr(self.model, "created_at"))
        self.assertTrue(hasattr(self.model, "updated_at"))

    def test_atrr(self):
        my_user = self.model
        self.assertTrue(hasattr(my_user, "email"))
        self.assertTrue(hasattr(my_user, "password"))
        self.assertTrue(hasattr(my_user, "first_name"))
        self.assertTrue(hasattr(my_user, "last_name"))

    def test_to_dict(self):
        my_user = self.model
        my_user.email = "bsalazarperdomo@gmail.com"
        my_user.password = "*****123"
        my_user.first_name = "Brayan"
        my_user.last_name = "Steven"
        my_model_json = my_user.to_dict()
        attrs = ["id",
                 "created_at",
                 "updated_at",
                 "email",
                 "password",
                 "first_name",
                 "last_name",
                 "__class__"]
        self.assertCountEqual(my_model_json.keys(), attrs)
        self.assertEqual(my_model_json['__class__'], 'User')
        self.assertEqual(my_model_json['email'], "bsalazarperdomo@gmail.com")
        self.assertEqual(my_model_json['password'], "*****123")
        self.assertEqual(my_model_json['first_name'], "Brayan")
        self.assertEqual(my_model_json['last_name'], "Steven")

    def test_to_dict_values(self):
        format = "%Y-%m-%dT%H:%M:%S.%f"
        my_model = self.model
        my_model_json = my_model.to_dict()
        self.assertEqual(my_model_json["__class__"], "User")
        self.assertEqual(type(my_model_json["created_at"]), str)
        self.assertEqual(type(my_model_json["updated_at"]), str)
        self.assertNotEqual(my_model_json["created_at"],
                            my_model.created_at)
        self.assertNotEqual(my_model_json["updated_at"],
                            my_model.updated_at)
