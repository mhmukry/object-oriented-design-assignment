import random #importing random generator module
from Salesmanagement import Salesmanagement

class Product:
    def __init__(self, product_code, product_name):
        self.product_code = product_code
        self.product_name = product_name

    def get_product_code(self):
        return self.product_code

    def get_product_name(self):
        return self.product_name
 