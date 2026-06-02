# Initialize the inventory dictionary with stock details
inventory = {
    "Bread": [30, 50, 10, False],   # "Item": [current stock, minimum stock, restock quantity, on sale (True/False)]
    "Eggs": [120, 200, 40, False],
    "Milk": [60, 100, 20, False],
    "Apples": [15, 50, 15, False]
}

discount_threshold = 100
# j=0
# Item = ["current stock", "minimum stock", "restock quantity", "on sale (True/False)"]

print("Processing started")

for item_name in inventory:
    print(item_name)
    for i in range(len(inventory[item_name])):
        print(inventory[item_name][i])

print("Processing Bread :")
while inventory["Bread"][0] < inventory["Bread"][1]:
    inventory["Bread"][0] += inventory["Bread"][2]
    if inventory["Bread"][0] > discount_threshold and not inventory["Bread"][3]:
        inventory["Bread"][3] = True

print("Processing Eggs :")
while inventory["Eggs"][0] < inventory["Eggs"][1]:
    inventory["Eggs"][0] += inventory["Eggs"][2]
    if inventory["Eggs"][0] > discount_threshold and not inventory["Eggs"][3]:
        inventory["Eggs"][3] = True

print("Processing Milk :")
while inventory["Milk"][0] < inventory["Milk"][1]:
    inventory["Milk"][0] += inventory["Milk"][2]
    if inventory["Milk"][0] > discount_threshold and not inventory["Milk"][3]:
        inventory["Milk"][3] = True

print("Processing Apples :")
while inventory["Apples"][0] < inventory["Apples"][1]:
    inventory["Apples"][0] += inventory["Apples"][2]
    if inventory["Apples"][0] > discount_threshold and not inventory["Apples"][3]:
        inventory["Apples"][3] = True

print("Processing completed")

