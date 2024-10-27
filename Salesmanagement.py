import random #importing random generator module

class Salesmanagement:
    def __init__(self,  sale_price, manufacture_cost, estimated_monthly_units):

        self.sale_price = sale_price
        self.manufacture_cost = manufacture_cost
        self.estimated_monthly_units = estimated_monthly_units


    def get_sale_price(self):
        return self.sale_price    
    
    def get_manufacture_cost(self):
        return self.manufacture_cost   

    def get_estimated_monthly_units(self):
        return self.estimated_monthly_units   

   