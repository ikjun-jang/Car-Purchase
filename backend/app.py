from flask import Flask, jsonify, request, abort
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from flask_migrate import Migrate
import datetime
import pytz

from models import setup_db, db, Purchase
from enums import Battery, Wheel, Tire

def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__)
    setup_db(app)
    CORS(app)

    # to migrate the database
    migrate = Migrate(app, db)

    BASE_PRICE = 12
    DISCOUNT_AMOUNT = 2

    def calc_battery(type):
        price = 0
        if type == Battery.KWH_40: price = 0
        elif type == Battery.KWH_60: price = 2.5
        elif type == Battery.KWH_80: price = 6
        return price

    def calc_wheel(type):
        price = 0
        if type == Wheel.MODEL_1: price = 0
        elif type == Wheel.MODEL_2: price = 150
        elif type == Wheel.MODEL_3: price = 350
        return price

    def calc_tire(type):
        price = 0
        if type == Tire.ECO: price = 0
        elif type == Tire.PERFORMANCE: price = 80
        elif type == Tire.RACING: price = 150
        return price
    
    def check_discount():
        result = False

        tz = pytz.timezone('Europe/Berlin')
        now = datetime.datetime.now(tz)
        long_months = [1, 3, 5, 7, 8, 10, 12]
        short_months = [4, 6, 9, 11]
         
        if now.weekday() == 4:
            if now.month in long_months and now.day >= 25:
                result = True
            elif now.month in short_months and now.day >= 24:
                result = True
            elif now.month == 2 and now.year % 4 == 0 and now.day >= 23:
                result = True
            elif now.month == 2 and now.year % 4 != 0 and now.day >= 22:
                result = True

        return result

    def calc_price(battery, wheel, tire):
        battery_price = calc_battery(battery)
        wheel_price = calc_wheel(wheel)
        tire_price = calc_tire(tire)
        total_price = BASE_PRICE + battery_price + wheel_price + tire_price

        if check_discount():
            total_price = total_price - DISCOUNT_AMOUNT
        
        return total_price

    def check_purchase_validity(battery, wheel, tire):
        validity = True
        
        if wheel == Wheel.MODEL_3 and battery < Battery.KWH_60:
            validity = False
        if tire == Tire.PERFORMANCE and wheel < Wheel.MODEL_2:
            validity = False
        if tire == Tire.RACING and wheel < Wheel.MODEL_3:
            validity = False

        return validity

    '''
    Endpoint to post a new car purchase,
    which will require battery, wheel and tire info
    '''
    @app.route("/configure", methods=["POST"])
    def create_purchase():
        body = request.get_json()
        battery = int(body['battery'])
        wheel = int(body['wheel'])
        tire = int(body['tire'])

        total_price = calc_price(battery, wheel, tire)

        if check_purchase_validity(battery, wheel, tire) == False:
            abort(422)
        
        try:
            new_puchase = Purchase (
                user_name = body['user_name'],
                battery = Battery(battery).name,
                wheel = Wheel(wheel).name,
                tire = Tire(tire).name,
                price = str(total_price) + " euro"
            )
            new_puchase.insert()

            return jsonify(
                {
                    "success": True,
                    "total_price": total_price,
                    "purchase": new_puchase.format()
                }
            )
        except:
            abort(422)

    '''
    Handling GET requests to fetch 
    all reports of purchases
    This endpoint should return a list of purchases, 
    number of total purchases
    '''
    @app.route("/report")
    def retrieve_purchase():
        # to fetch all purchases
        purchases = Purchase.query.order_by(Purchase.id).all()
        purchase_list = [purchase.format() for purchase in purchases]

        return jsonify(
            {
                "success": True,
                "purchases": purchase_list,
                "total_purchase": len(purchase_list),
            }
        )

    # Error Handling
    '''
    Error handler for entity not found
    '''
    @app.errorhandler(404)
    def not_found(error):
        return jsonify({
            "success": False,
            "error": 404,
            "message": "resource not found"
        }), 404

    '''
    Error handling for unprocessable entity
    '''
    @app.errorhandler(422)
    def unprocessable(error):
        return jsonify({
            "success": False,
            "error": 422,
            "message": "unprocessable"
        }), 422

    return app

APP = create_app()

if __name__ == '__main__':
    #APP.debug = True
    APP.run()