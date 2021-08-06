from flask_restplus import fields
from server.instance import server

# instance of a Api
shipping_ns = server.shipping_ns

# model of exchange data in JSON
dimensao = shipping_ns.model('Dimensao', {
    "altura": fields.Integer(description=102),
    "largura": fields.Integer(description=40),
})

product = shipping_ns.model('Product',{
    "dimensao": fields.Nested(dimensao),
    "peso": fields.Integer(description=400)
})
