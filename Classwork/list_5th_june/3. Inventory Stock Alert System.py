#3. Inventory Stock Alert System
# Initial inventory stock quantities
stock = [25, 5, 0, 12, 3, 18, 0, 30]

# Initialize lists and counters
out_of_stock_count = 0
restock_list = []
available_products_count = 0
high_stock_list = []

# Process the stock quantities
for qty in stock:
    # 1. Count products that are out of stock (quantity == 0)
    if qty == 0:
        out_of_stock_count += 1
        
    # 2. Check for products that need restocking (quantity < 10)
    if qty < 10:
        restock_list.append(qty)
        
    # 3. Count available products (quantity > 0)
    if qty > 0:
        available_products_count += 1
        
    # 4. Create list for high stock products (quantity >= 15)
    if qty >= 15:
        high_stock_list.append(qty)

# Display the results
print(f"Out of Stock Products: {out_of_stock_count}")
print(f"Restock Required: {restock_list}")
print(f"Available Products Count: {available_products_count}")
print(f"High Stock List (>= 15): {high_stock_list}")
