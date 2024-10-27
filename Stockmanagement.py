import random #importing random generator module
from Profitmanagement import Profitmanagement

class Stockmanagement:
    def __init__(self, product_code, product_name, sale_price, manufacture_cost, stock_level, estimated_monthly_units):
        self.product_code = product_code
        self.product_name = product_name
        self.sale_price = sale_price
        self.manufacture_cost = manufacture_cost
        self.stock_level = stock_level
        self.estimated_monthly_units = estimated_monthly_units

    def get_monthly_stock_report(self):
        report = []
        total_units_sold = 0
        total_units_manufactured = 0

        for month in range(1, 13):
            units_manufactured = self.estimated_monthly_units
            units_sold = random.randint(max(0, units_manufactured - 10), units_manufactured + 10)

            unavailable_units_for_sale = 0

            # Check if the stock is enough to fulfill the sale
            if self.stock_level < units_sold:
                unavailable_units_for_sale = units_sold - self.stock_level
                units_sold = self.stock_level  # Sell only available stock
                
            self.stock_level -= units_sold
            total_units_sold += units_sold
            total_units_manufactured += units_manufactured
            self.stock_level += units_manufactured  # Add manufactured units to stock
            report.append((month, self.stock_level, units_sold, units_manufactured, unavailable_units_for_sale))

            self.profitmanagement = Profitmanagement(total_units_sold, total_units_manufactured, self.sale_price, self.manufacture_cost)

   
            net_profit = self.profitmanagement.get_net_profit()
        return report, net_profit
