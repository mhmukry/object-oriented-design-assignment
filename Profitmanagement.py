import random #importing random generator module

class Profitmanagement:
    def __init__(self, total_units_sold, total_units_manufactured, sale_price, manufacture_cost):
        self.total_units_sold = total_units_sold
        self.sale_price = sale_price
        self.manufacture_cost = manufacture_cost
        self.total_units_manufactured = total_units_manufactured


    def get_net_profit(self):
 

        net_profit = (self.total_units_sold * self.sale_price) - (self.total_units_manufactured * self.manufacture_cost)
        return  net_profit