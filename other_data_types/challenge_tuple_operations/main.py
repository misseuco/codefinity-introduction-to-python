# Current inventory on shelf
shelf = ("apples", "oranges", "bananas", "apples", "grapes", "bananas", "apples")
apple_count = shelf.count("apples")
print(f"Number of Apples: {apple_count}")
banana_index = shelf.index("bananas")
print(f"First Banana Index: {banana_index}")
number_of_apples = shelf.count("apples")
if number_of_apples < 5:
    print("Apples need to be restocked.")
else:
    print("Apples are sufficiently stocked.")

number_of_grapes = shelf.count("grapes")
if number_of_grapes == 1:
    print("Grapes need to be restocked.")
else:
    print("Grapes are sufficiently stocked.")

if "oranges" in shelf:
    oranges_index = shelf.index("oranges")
    print(f"Oranges are at index : {oranges_index}")
else:
    print("Oranges are out of stock.")