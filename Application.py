from Product import Product
from Salesmanagement import Salesmanagement
from Stockmanagement import Stockmanagement

class Application:
    def __init__(self):
        self.product = None
        self.salesmanagement = None
        self.stockmanagement = None

    def get_user_input(self):
        product_code = self.get_user_input_integer("Enter product code (100-1000): ", 100, 1000) 
        product_name = input("Enter product name: ")
        sale_price = self.get_user_input_float_min_or_max("Enter product sale price (greater than zero): ","minimum",1)
        manufacture_cost = self.get_user_input_float_min_or_max("Enter product manufacture cost (greater than zero): ", "minimum",1)
        stock_level = self.get_user_input_integer_min_or_max("Enter stock level (greater than 0): ","minimum",1)
        estimated_monthly_units = self.get_user_input_integer_min_or_max("Enter estimated monthly units manufactured (0 or greater): ","minimum",1)
 
        self.salesmanagement = Salesmanagement(sale_price, manufacture_cost, estimated_monthly_units) 
        self.product = Product(product_code, product_name)
        self.stockmanagement = Stockmanagement(product_code, product_name, sale_price, manufacture_cost, stock_level, estimated_monthly_units)

    
    def get_user_input_integer(self,  input_str,  min_value,  max_value):
        while (1):
            input_integer = int(input(input_str))
            if ((input_integer >= min_value) and (input_integer <= max_value)):
                return input_integer
            else:
                print("Incorrect value")

    def get_user_input_integer_min_or_max(self,  input_str,  value_type, value):
        while (1):
            input_integer = int(input(input_str))
            if value_type == "minimum":
                if (input_integer >= value):
                    return input_integer
                else:
                    print("Incorrect value")
            elif value_type == "maximum":
                if (input_integer <= value):
                    return input_integer
                else:
                    print("Incorrect value")

    def get_user_input_float_min_or_max(self,  input_str,  value_type, value):
        while (1):
            input_float = float(input(input_str))
            if value_type == "minimum":
                if (input_float >= value):
                    return input_float
                else:
                    print("Incorrect value")
            elif value_type == "maximum":
                if (input_float <= value):
                    return input_float
                else:
                    print("Incorrect value")

    def display_report(self):
        report, net_profit = self.stockmanagement.get_monthly_stock_report()
        print("\nPredicted Monthly Stock Statement:")
        print("Programming principles sample stock statement")
        
        print("Product code:")
        print(self.product.get_product_code())
        print("Product name: ")
        print(self.product.get_product_name())
           
        print("Sale price (in CAD):")
        print(self.salesmanagement.get_sale_price())       
        print("Manufacture cost (in CAD):")
        print(self.salesmanagement.get_manufacture_cost())             
        print("Monthly production units:")
        print(self.salesmanagement.get_estimated_monthly_units())     

        for month, stock, sold, manufactured, unavailable_units_for_sale in report:
            print(f"Month {month}: ")
            print(f"|      Manufactured:                {manufactured} units")
            print(f"|      sold:                        {sold} units")
            print(f"|      stock:                       {stock} units")
            if unavailable_units_for_sale > 0:
                print(f"|      unavailable_units_for_sale:  {unavailable_units_for_sale} units")

        print(f"Net Profit: {net_profit} CAD")

    def run(self):
        self.get_user_input()
        self.display_report()

if __name__ == "__main__":
    app = Application()
    app.run()