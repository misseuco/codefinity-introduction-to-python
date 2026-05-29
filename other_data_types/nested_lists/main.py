vegetables = ["tomatoes", "potatoes", "onions"]
vegetables.remove("onions")
vegetables.append("carrots")
vegetables.append("cucumbers")
vegetables.sort()
print(f"Updated Vegetable Inventory: {vegetables}")
if "carrots" in vegetables:
    print("Carrots are already in the list.")
if "cucumbers" in vegetables:
    print("cucumbers are already in the list.")