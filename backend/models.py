import os
from sqlalchemy import Column, ForeignKey, String, Integer
from flask_sqlalchemy import SQLAlchemy

'''
Database credentials handled using the dynamic environment variables
'''
database_path = os.getenv('DATABASE_URL', "postgresql://postgres:1701@localhost:5432/car")

db = SQLAlchemy()

"""
setup_db(app)
    binds a flask application and a SQLAlchemy service
"""
def setup_db(app, database_path=database_path):
    app.config["SQLALCHEMY_DATABASE_URI"] = database_path
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.app = app
    db.init_app(app)
    db.create_all()

class Purchase(db.Model):
    __tablename__ = "purchases"

    id = Column(Integer, primary_key=True)
    user_name = Column(String)
    battery = Column(String)
    wheel = Column(String)
    tire = Column(String)
    price = Column(String)

    def __init__(self, user_name, battery, wheel, tire, price):
        self.user_name = user_name
        self.battery = battery
        self.wheel = wheel
        self.tire = tire
        self.price = price

    def insert(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def format(self):
        return {
            "id": self.id,
            "user_name": self.user_name,
            "battery": self.battery,
            "wheel": self.wheel,
            "tire": self.tire,
            "price" : self.price,
        }