from os import name
from server.instance import server
from flask_restplus import fields

import json

# json shipping options
file_options_shipping = 'server\options_shipping.json'

# instance of a Api
shipping_ns = server.shipping_ns

shipping = shipping_ns.model('shipping',{
    "nome": fields.String(description='Entrega Ninja'),
    "valor_shipping": fields.Integer(description=8.00),
    "prazo_dias": fields.Integer(description=4),
})

class Shipping():

    def __init__(self, name, shipping_value, deadline_days):
        self.name = name
        self.shipping_value = shipping_value
        self.deadline_days = deadline_days
    
    def json(self, ):
        return { "nome": self.name, "valor_frete": self.shipping_value, "prazo_dias": self.deadline_days }
    
    @classmethod
    def validations_max_min_height(self, product_height, option_min_height, option_max_height):
        if (product_height >= option_min_height) and (product_height <= option_max_height): return True
        else: return False

    @classmethod
    def validations_max_min_width(self, product_width, option_min_width, option_max_width):
        if (product_width >= option_min_width) and (product_width <= option_max_width): return True
        else: return False
    
    @classmethod
    def validation_weight(self, product_weight):
        if product_weight > 0: return True
        else: return False
    
    @classmethod
    def freight_calculation(self, product_weight, const_freight):
        try:
            freight_value = (product_weight * const_freight) / 10
            return freight_value
        except: return 0
    
    @classmethod
    def calculate_shipping(self, cls):

        # data product
        product_height = float(cls['dimensao']['altura'])
        product_width = float(cls['dimensao']['largura'])
        product_weight = float(cls['peso'])
        
        list_freight = []
        
        with open(file_options_shipping, "r") as read_file:
            options_shipping = json.load(read_file)

            # percorre o arquivo json onde contém todos os tipos de entregas da KaBuM!
            for op_ship in options_shipping:
                option_min_height = float(op_ship['altura_minima'])
                option_max_height = float(op_ship['altura_maxima'])
                option_min_width = float(op_ship['largura_minima'])
                option_max_width = float(op_ship['largura_maxima'])
                
                validation_height = Shipping.validations_max_min_height(product_height, option_min_height, option_max_height)
                validation_width = Shipping.validations_max_min_width(product_width, option_min_width, option_max_width)
                validation_weight = Shipping.validation_weight(product_weight)
                
                if validation_height and validation_width and validation_weight: 
                    option_name = str(op_ship['tipo_entrega'])
                    delivery_deadline = int(op_ship['prazo_entrega'])
                    const_freight = float(op_ship['const_calculo_frete'])
                    
                    freight_value = Shipping.freight_calculation(product_weight, const_freight)
                    
                    shipping = Shipping(option_name, freight_value, delivery_deadline)

                    shipping_json = json.dumps(shippings)
                    # serialize to JSON
                    shipping_json = shipping_json.dum
                    list_freight.append(shipping_json)

        return list_freight

