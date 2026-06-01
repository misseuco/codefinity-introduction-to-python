prices = [29.99, 45.50, 12.75, 38.20]
# discount = [0.10, 0.20, 0.15, 0.05]

for i in range(len(prices)):
    # new_price = prices[i] * (1-discount[i])
    if i == 0:
        new_price = prices[i] * (1 - 0.10)
        prices[i] = new_price
        print(f"Updated price for item {i}: ${new_price:.2f}")
    elif i == 1:
        new_price = prices[i] * (1 - 0.20)
        prices[i] = new_price
        print(f"Updated price for item {i}: ${new_price:.2f}")
    elif i == 2:
        new_price = prices[i] * (1 - 0.15)
        prices[i] = new_price
        print(f"Updated price for item {i}: ${new_price:.2f}")
    elif i == 3:
        new_price = prices[i] * (1 - 0.05)
        prices[i] = new_price
        print(f"Updated price for item {i}: ${new_price:.2f}")
