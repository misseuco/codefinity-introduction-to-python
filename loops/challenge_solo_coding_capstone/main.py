# Inventory dictionary with stock, price, and discount price
inventory = {
    "Bread": [42, 1.20, 0.99],  # "Item": [current stock, regular price, discounted price]
    "Eggs": [225, 2.12, 1.99],  # Eggs should be sold at a discount
    "Apples": [9, 1.50, 1.35]   # Apples need to be restocked
}

Item = ["current stock", "regular price", "discounted price"]

for item in inventory:
    print(item)
print("-------------------------------")
print("Item Breag :")
if inventory["Bread"][0] < 30:
    print(f"Bread need restocking.")
elif inventory["Bread"][0] > 100:
    print(f"Bread should be sold at the discounted price of {inventory["Bread"][2]}.")
else:
    print(f"Bread should be sold at the regular price of {inventory["Bread"][1]}.")
print("-------------------------------")

print("Item Eggs :")
if inventory["Eggs"][0] < 30:
    print(f"Eggs need restocking.")
elif inventory["Eggs"][0] > 100:
    print(f"Eggs should be sold at the discounted price of {inventory["Eggs"][2]}.")
else:
    print(f"Eggs should be sold at the regular price of {inventory["Eggs"][1]}.")
print("-------------------------------")

print("Item Apples :")
if inventory["Apples"][0] < 30:
    print(f"Apples need restocking.")
elif inventory["Apples"][0] > 100:
    print(f"Apples should be sold at the discounted price of {inventory["Apples"][2]}.")
else:
    print(f"Apples should be sold at the regular price of {inventory["Apples"][1]}.")
