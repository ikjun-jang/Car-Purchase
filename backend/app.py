from flask import Flask, jsonify, request, abort
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from flask_migrate import Migrate

from models import setup_db, db, Purchase

def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__)
    setup_db(app)
    CORS(app)

    # to migrate the database
    migrate = Migrate(app, db)

    @app.route("/")
    def test():
        return "hello"

    return app

APP = create_app()

if __name__ == '__main__':
    APP.debug = True
    APP.run()