import random #importing random generator module

class Product:
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

            # Check if the stock is enough to fulfill the sale
            if self.stock_level < units_sold:
                units_sold = self.stock_level  # Sell only available stock
            self.stock_level -= units_sold
            total_units_sold += units_sold
            total_units_manufactured += units_manufactured
            self.stock_level += units_manufactured  # Add manufactured units to stock
            report.append((month, self.stock_level, units_sold, units_manufactured))

        net_profit = (total_units_sold * self.sale_price) - (total_units_manufactured * self.manufacture_cost)
        return report, net_profit

class Application:
    def __init__(self):
        self.product = None

    def get_user_input(self):
        product_code = int(input("Enter product code (100-1000): "))
        product_name = input("Enter product name: ")
        sale_price = float(input("Enter product sale price (greater than zero): "))
        manufacture_cost = float(input("Enter product manufacture cost (greater than zero): "))
        stock_level = int(input("Enter stock level (greater than 0): "))
        estimated_monthly_units = int(input("Enter estimated monthly units manufactured (0 or greater): "))

        self.product = Product(product_code, product_name, sale_price, manufacture_cost, stock_level, estimated_monthly_units)

    def display_report(self):
        report, net_profit = self.product.get_monthly_stock_report()
        print("\nPredicted Monthly Stock Statement:")
        for month, stock, sold, manufactured in report:
            print(f"Month {month}: Stock Level {stock}, Units Sold {sold}, Units Manufactured {manufactured}")
        print(f"Net Profit: {net_profit}")

    def run(self):
        self.get_user_input()
        self.display_report()

if __name__ == "__main__":
    app = Application()
    app.run()