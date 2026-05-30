grocery_inventory = {
    "Milk": ("Dairy", 3.50, 8),
    "Eggs": ("Dairy", 5.50, 30),
    "Bread": ("Bakery", 2.99, 15),
    "Apples": ("Produce", 1.50, 50),
}
egg_price = grocery_inventory["Eggs"][1]
if egg_price > 5:
    print("Eggs are too expensive, reducing the price by $1.")
    grocery_inventory.update({"Eggs": ("Dairy", egg_price - 1, 30)})
else:
    print("The price of Eggs is reasonable.")

grocery_inventory.update({"Tomatoes": ("Produce", 1.20, 30)})
print(f"Inventory after adding Tomatoes: {grocery_inventory}")

milk_stock = grocery_inventory["Milk"][2]
if milk_stock < 10:
    grocery_inventory.update({"Milk": ("Dairy", 3.50, milk_stock + 20)})
    print("Milk needs to be restocked. Increasing stock by 20 units.")
else:
    print("Milk has sufficient stock.")

apple_price = grocery_inventory["Apples"][1]
if apple_price > 2:
    grocery_inventory.pop("Apples")
    print("Apples removed from inventory due to high price.")

print(f"Updated inventory: {grocery_inventory}")