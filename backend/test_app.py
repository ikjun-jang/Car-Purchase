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
        self.database_path = os.getenv('DATABASE_TEST_URL', "postgresql://postgres:1701@localhost:5432/library_test")

        setup_db(self.app, self.database_path)

        # to test successful result
        self.new_purchase = {"battery": "40 kwh", "wheel": "model1", "tire": "eco"}

        # to test unsuccessful
        self.invalid_purchase = {"battery": "40 kwh", "wheel": "model3", "tire": "racing"}

        # binds the app to the current context
        with self.app.app_context():
            self.db = SQLAlchemy()
            self.db.init_app(self.app)
            # create all tables
            self.db.create_all()

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

    def test_purchase_car(self):
        res = self.client().post("/configure", json=self.new_purchase)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data["success"], True)

    def test_422_sent_invalid_purchase_info(self):
        res = self.client().post("/configure", json=self.invalid_purchase)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 422)
        self.assertEqual(data["success"], False)
        self.assertEqual(data["message"], "unprocessable")

    def tearDown(self):
        """Executed after reach test"""
        pass

# Make the tests conveniently executable
if __name__ == "__main__":
    unittest.main()
