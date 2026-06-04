# List of product names
products = ["Banana", "Apple", "Mango", "Cherry"]

# List of product prices
prices = [1.20, 0.50, 2.50, 1.75]

# List of quantity sold
quantities_sold = [50, 100, 25, 40]

i = 0

combined_list = list(zip(products,prices,quantities_sold))

sorted_products = sorted(combined_list)

print(sorted_products)
for product in sorted_products:
    # print(product)
    print(f"product: {product[0]}, Price: {product[1]}, Quantity Sold: {product[2]}")

    


    