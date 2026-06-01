produce = ["Tomatoes", "Lettuce"]
dairy = ["Milk", "Cheese"]

groceries = [produce] + [dairy]

for i in range(2):
    print(f"Section {i}")
    for item in groceries[i]:
        print(f"Item name: {item}")
# print(groceries)
