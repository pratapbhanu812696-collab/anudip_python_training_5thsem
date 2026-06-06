# Initial data
orders = [
    ("Laptop", 55000),
    ("Mouse", 800),
    ("Keyboard", 1500),
    ("Monitor", 12000),
    ("Pen Drive", 600)
]

# Variables to keep track of our totals and counts
total_value = 0
below_1000_count = 0

# Variables to track the most expensive product
most_expensive_product = ""
highest_price = 0

print("--- Products costing more than ₹1000 ---")

# Go through each order one by one
for product, price in orders:
    
    # 1. Check and display if the product costs more than ₹1000
    if price > 1000:
        print("-", product)
        
    # 2. Check if this is the most expensive product we've seen so far
    if price > highest_price:
        highest_price = price
        most_expensive_product = product
        
    # 3. Add the current product's price to the total order value
    total_value = total_value + price
    
    # 4. Check if the product costs below ₹1000 to increase our count
    if price < 1000:
        below_1000_count = below_1000_count + 1

print("---------------------------------------")

# Print the final results
print("Most expensive product:", most_expensive_product)
print("Total order value: ₹", total_value)
print("Number of products below ₹1000:", below_1000_count)
