from halloween import City, CostumeShop, Customer

# Simulation setup

city = City("Chiatura", 5000)

# Create shops
shop1 = CostumeShop("Gogias Chinchebi")
shop1.add_costume("Skeleton Costume", 50, 30)
shop1.add_costume("Vampire Costume", 30, 40)
shop1.add_costume("Zombie Costume", 20, 25)

shop2 = CostumeShop("Sherekilebis Samosi")
shop2.add_costume("Ghost Costume", 40, 20)
shop2.add_costume("Pumpkin Costume", 15, 35)
shop2.add_costume("Mummy Costume", 25, 30)

# Add shops to city
city.add_shop(shop1)
city.add_shop(shop2)

# Simulate demand based on population
city.simulate_demand()

# Create customers
customer1 = Customer("Alice", 100, ["Skeleton Costume", "Zombie Costume"])
customer2 = Customer("Bob", 85, ["Vampire Costume", "Ghost Costume"])

# Customers shop
for costume in customer1.shopping_list:
    for shop in city.costume_shops:
        if costume in shop.costumes and shop.costumes[costume] > 0:
            customer1.buy_costume(shop, costume, 1)

for costume in customer2.shopping_list:
    for shop in city.costume_shops:
        if costume in shop.costumes and shop.costumes[costume] > 0:
            customer2.buy_costume(shop, costume, 1)

# Generate report
print(city.report())
print(customer1.shop_report())
print(customer2.shop_report())