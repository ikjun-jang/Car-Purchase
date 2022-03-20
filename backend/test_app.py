import os
import unittest
import json
from flask_sqlalchemy import SQLAlchemy

from app import create_app
from models import setup_db, Purchase

class BookTestCase(unittest.TestCase):

    def setUp(self):
        """Define test variables and initialize app"""
        self.app = create_app()
        self.client = self.app.test_client

        """ 
        Database credentials handled using the dynamic environment variables 
        """
        self.database_path = os.getenv('DATABASE_TEST_URL', "postgresql://postgres@localhost:5432/car_test")

        setup_db(self.app, self.database_path)

        # to test successful result
        self.new_purchase = {"user_name": "Winfrey", "battery": 2, "wheel": 2, "tire": 2}

        # to test unsuccessful
        self.invalid_purchase_1 = {"user_name": "Winfrey", "battery": 1, "wheel": 3, "tire": 3}
        self.invalid_purchase_2 = {"user_name": "Winfrey", "battery": 3, "wheel": 2, "tire": 3}

        # binds the app to the current context
        with self.app.app_context():
            self.db = SQLAlchemy()
            self.db.init_app(self.app)
            # create all tables
            self.db.create_all()

    def test_purchase_car(self):
        res = self.client().post("/configure", json=self.new_purchase)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data["success"], True)

    def test_422_sent_invalid_purchase_info_1(self):
        res = self.client().post("/configure", json=self.invalid_purchase_1)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 422)
        self.assertEqual(data["success"], False)
        self.assertEqual(data["message"], "unprocessable")
    
    def test_422_sent_invalid_purchase_info_2(self):
        res = self.client().post("/configure", json=self.invalid_purchase_2)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 422)
        self.assertEqual(data["success"], False)
        self.assertEqual(data["message"], "unprocessable")

    def test_get_report(self):
        res = self.client().get("/report")
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data["success"], True)

    def test_404_requesting_invalid_address_to_report(self):
        res = self.client().get("/reports")
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertEqual(data["success"], False)
        self.assertEqual(data["message"], "resource not found")

    def tearDown(self):
        """Executed after reach test"""
        pass

# Make the tests conveniently executable
if __name__ == "__main__":
    unittest.main()
