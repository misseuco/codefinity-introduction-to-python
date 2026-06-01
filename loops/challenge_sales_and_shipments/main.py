# List of products with their initial stock levels at the start of the week
products = [
    ["Apples", 150],  
    ["Bananas", 200],
    ["Oranges", 100],
    ["Mangoes", 120]
]

# List of products sold by the end of the week
units_sold = [["Apples", 30], ["Bananas", 45], ["Oranges", 20], ["Mangoes", 10]]
# New shipment received at the end of the week
shipment_received = [["Apples", 50], ["Bananas", 70], ["Oranges", 30], ["Mangoes", 40]]

for i in range(len(products)):
    product_name = products[i][0]
    sold_units = units_sold[i][1]
    sold_inits = products[i][1]
    sold_for_each_product = products[i][1] - units_sold[i][1]
    print(f"Solde for each product : is {sold_for_each_product:.2f}")
    
for i in range(len(products)):
    products[i][1] = products[i][1] - units_sold[i][1] + shipment_received[i][1]

print(f"Final stock levels for all products: {products}")