from flask import request
from flask_restplus import Resource
import json

from server.instance import server
from models.shipping import shipping, Shipping
from models.product import product

# instance of a Api
shipping_ns = server.shipping_ns

class ShippingRoute(Resource):
    # validation of a payload
    @shipping_ns.expect(product)
    @shipping_ns.doc('Calculate de shipping')   
    def post(self, ):
        try:
            product_data = shipping_ns.payload
            
            shippings = Shipping.calculate_shipping(product_data)
            
            # serialize data shipping to JSON
            print(shippings)
            json_list_freight = json.dumps(shippings)
            print(json_list_freight)
            return json_list_freight, 201
        except:
            return {"message": "Error in calculate freight!"}

     
