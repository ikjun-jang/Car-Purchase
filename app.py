from flask import Flask, jsonify
#from flask_cors import CORS

def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__)
    #CORS(app)

    @app.route("/")
    def test():
        return "hello"

    return app

APP = create_app()

if __name__ == '__main__':
    APP.debug = True
    APP.run()