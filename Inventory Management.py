# Inventory Management

stock = [0, 5, 20, 8, 15, 0, 3, 50]

# Remove items with 0 stock
stock = [item for item in stock if item > 0]

# Restock items below 10
for i in range(len(stock)):
    if stock[i] < 10:
        stock[i] += 50

# Total inventory count
total_inventory = sum(stock)

print("Updated Stock:", stock)
print("Total Inventory Count:", total_inventory)