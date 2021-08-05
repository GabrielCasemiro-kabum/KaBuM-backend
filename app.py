from flask import jsonify
from marshmallow import ValidationError

from ma import ma
from controllers.shipping import ShippingRoute

from server.instance import server

api = server.api
app = server.app

api.add_resource(ShippingRoute, '/fretes')

if __name__ == '__main__':
    ma.init_app(app)
    server.run()