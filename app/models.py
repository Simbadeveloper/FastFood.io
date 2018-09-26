"""
app/models.py
"""

orders = []

class Order(object):
    """class Order """

    def __init__(self, name, price, quantinty):
        """initialize """
        self.orderid = len(orders)+1
        self.name = name
        self.price = price
        self.quantinty = quantinty




    def create_order(self):
        """ create order that will be used later """
        order = {
            "orderid":len(orders)+1,
            "name": self.name,
            "price": self.price,
            "quantity": self.quantity

        }

        orders = [
            {
                "orderid": 1,
                "name": "Rice",
                "price": 200,
                "quantity": 1

            },
            {
                "orderid": 2,
                "name": "pilau",
                "price": 100,
                "quantity": 1,
            }]

        orders = orders.append(order)

        return order


    @staticmethod
    def get_all():
        """ get_all: lists all orders """
        orders = [
            {
                "orderid": 1,
                "name": "Rice",
                "price": 200,
                "quantity": 1

            },
            {
                "orderid": 2,
                "name": "pilau",
                "price": 100,
                "quantity": 1,
            }]
        return orders

    def delete(self):
        """ delete code """
        orders = [
            {
                "orderid": 1,
                "name": "Rice",
                "price": 200,
                "quantity": 1

            },
            {
                "orderid": 2,
                "name": "pilau",
                "price": 100,
                "quantity": 1,
            }
         ]

        order =[order for order in orders if (order['orderid'])==orderid]
        del order['orderid']
        del orders['name']
        del orders['price']
        del order['quantity']
        return orders



    def __repr__(self):
        return "<Order: {}>".format(self.orderid, self.name, self.price, self.quantity)
