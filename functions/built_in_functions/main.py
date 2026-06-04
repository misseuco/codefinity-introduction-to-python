# Dictionary of products with price and quantity sold as strings
products = {
    "Apple": ["1.20", "50"],   # "Item": [price, quantity sold]
    "Banana": ["0.50", "100"],
    "Cherry": ["2.50", "25"],
    "Mango": ["1.75", "40"]
}
total_sales_list = []

for product, details in products.items():
    print(f"Product : {product}; Details : {details}")
    print(f"Price_To_Float : {float(details[0]):.2f}")
    products[product][0] = float(details[0])
    print(f"Quantity_To_Int : {int(details[1])}")
    products[product][1] = float(details[1])
    total_sales = products[product][0] * products[product][1]
    #print(total_sales)
    print(f"Total sales for {product}: ${total_sales}")
    total_sales_list.append(total_sales)
print(total_sales_list)
total_sum = sum(total_sales_list)
#print(total_sum)
print(f"Total sum of all sales: ${total_sum}")
min_sales = min(total_sales_list)
#print(min_sales)
print(f"Minimum sales: ${min_sales}")
max_sales = max(total_sales_list)
#print(max_sales)
print(f"Maximum sales: ${max_sales}")
