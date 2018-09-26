# app/__init__.py
from flask_api import FlaskAPI
from flask import request, jsonify

# local import
from instance.config import app_config


def create_app(config_name):

    from app.models import Order

    app = FlaskAPI(__name__, instance_relative_config=True)
    app.config.from_object(app_config["development"])


    @app.route('/v1/orders', methods=['POST', 'GET'])
    def orders():
        if request.method == "POST":
            #POST
            name = str(request.args.get('name'))
            price = str(request.args.get('price'))
            quantity = str(request.args.get('quantity'))



            if name:
                order = Order(orderid=orderid, name=name, price=price, quantity=quantity)
                result = order.create_order()
                response = jsonify(result)
                response.status_code = 201
                return response

        else:
            # GET
            orders = Order.get_all()
            response = jsonify(orders)
            response.status_code = 200
            return response

    @app.route('/v1/orders/<orderid>', methods=['GET', 'PUT', 'DELETE'])
    def order_manipulation(orderid, **kwargs):
        # Get an order using it's orderid
        #get all order
        orders = Order.get_all()
        #filter through to get specific order
        order = [order for order in orders if(orders['orderid'])==orderid]
        response =jsonify(order)
        response.status.code == 200

        if request.method == 'DELETE':
            order = Order(orderid=orderid, name='', price='', quantity='')
            orders = order.delete()

            results = []
            order =[order for order in orders if(order['orderid']==orderid)]
            results.append(orders)

            message = {
            "message": "order {} deleted successfully".format(order.orderid)
            }
            print(message)

            response = jsonify(results)
            response.status_code = 200
            return response

        elif request.method == 'PUT':

            name = str(request.data.get('name'))
            price = str(request.data.get('price'))
            quantity = str(request.data.get('quantity'))

            order['name'] = name
            order['price'] = price
            order['quantity'] = quantity


            order = Order(orderid =orderid, name=order['name'], price=order['price'], quantity=order['quantity'])
            result = order.create_order()
            response = jsonify(result)
            response.status_code = 200
            return response
        else:
            # GET
            response = jsonify({
                'name': order['name'],
                'price': order['price'],
                'quantity': order['quantity'],

            })
            response.status_code = 200
            return response

    return app
