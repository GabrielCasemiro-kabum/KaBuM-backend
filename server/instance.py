from flask import Flask, Blueprint
from flask_restplus import Api

class Server():
    def __init__(self):
        self.app = Flask(__name__)
        self.bluePrint = Blueprint('api', __name__, url_prefix='/api')
        self.api = Api(self.bluePrint,
                        version='1.0', 
                        doc='/doc', 
                        title='Challenge KaBuM with Flask-RestPlus',
                        description='REST API that will be used by the website to query product transport options!')
        self.app.register_blueprint(self.bluePrint)

        self.app.config['JSON_SORT_KEYS'] = False

        self.shipping_ns = self.shipping_ns()

        super().__init__()

    def shipping_ns(self, ):
        return self.api.namespace(name='Shipping', description='shipping related operations', path='/')

    def run(self, ):
        self.app.run(
            port=5000,
            debug=True,
            host='0.0.0.0'
        )

server = Server()