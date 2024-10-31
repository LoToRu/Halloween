#Halloween Market

class CostumeShop:
    def __init__(self, name):
        self.name = name
        self.costumes = {}
        self.prices = {}
        self.demand = {}

    def add_costume(self, costume_name, stock, price):
        self.costumes[costume_name] = stock
        self.prices[costume_name] = price
        self.demand[costume_name] = 0

    def adjust_price(self, costume_name, new_price):
        if costume_name in self.prices:
            self.prices[costume_name] = new_price

    def adjust_stock(self, costume_name, new_stock):
        if costume_name in self.costumes:
            self.costumes[costume_name] = new_stock

    def adjust_demand(self, costume_name, population):
        if costume_name in self.demand:
            self.demand[costume_name] = min(population // 100, self.costumes[costume_name])  # Example logic

    def sell_costume(self, costume_name, quantity):
        if costume_name in self.costumes and self.costumes[costume_name] >= quantity:
            self.costumes[costume_name] -= quantity
            self.demand[costume_name] += quantity  # Increase demand based on sales
            new_price = self.prices[costume_name] * (1 + 0.1 * (self.demand[costume_name] / 10))  # Price increase based on demand
            self.adjust_price(costume_name, new_price)

    def report_stock(self):
        report = f"Shop: {self.name}\n"
        for costume in self.costumes:
            report += f"Costume: {costume}, Quantity: {self.costumes[costume]}, Price: ${round(self.prices[costume], 2)}, Demand: {self.demand[costume]}\n"
        return report


class City:
    def __init__(self, name, population):
        self.name = name
        self.population = population
        self.costume_shops = []

    def add_shop(self, shop):
        self.costume_shops.append(shop)

    def simulate_demand(self):
        for shop in self.costume_shops:
            for costume in shop.costumes:
                shop.adjust_demand(costume, self.population)

    def report(self):
        report = f"City: {self.name}, Population: {self.population}\nShops:\n"
        for shop in self.costume_shops:
            report += shop.report_stock() + "\n"
        return report


class Customer:
    def __init__(self, name, budget, shopping_list):
        self.name = name
        self.budget = budget
        self.shopping_list = shopping_list
        self.purchased_costumes = {}

    def check_budget(self, price, quantity):
        return self.budget >= price * quantity

    def buy_costume(self, shop, costume_name, quantity):
        if costume_name in shop.costumes and self.check_budget(shop.prices[costume_name], quantity):
            shop.sell_costume(costume_name, quantity)
            self.budget -= shop.prices[costume_name] * quantity
            self.budget = round(self.budget, 2)
            self.purchased_costumes[costume_name] = self.purchased_costumes.get(costume_name, 0) + quantity

    def shop_report(self):
        report = f"Customer: {self.name}, Budget: ${self.budget}\nPurchased Costumes:\n"
        for costume, quantity in self.purchased_costumes.items():
            report += f"{costume}: {quantity}\n"
        return report
