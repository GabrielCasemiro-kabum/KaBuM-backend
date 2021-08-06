from flask_restplus import Resource

from server.instance import server
from models.shipping import Shipping
from models.product import product

# instance of a Api
shipping_ns = server.shipping_ns

class ShippingRoute(Resource):
    # add model in doc
    @shipping_ns.expect(product)
    @shipping_ns.doc('Calculate de shipping')   
    def post(self, ):
        try:
            product_data = shipping_ns.payload
            
            shippings = Shipping.calculate_shipping(product_data)
            
            return shippings, 201
        except:
            return {"message": "Error in calculate freight!"}
